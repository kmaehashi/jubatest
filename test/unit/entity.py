# -*- coding: utf-8 -*-

import jubatus
import os
import tempfile

from jubatest import *
from jubatest.entity import JubaTestEnvironment, JubaNode, JubaRPCServer
from jubatest.unit import JubaSkipTest, JubaTestFixtureFailedError
from jubatest.exceptions import JubaTestAssertionError

class JubaTestEnvironmentTest(JubaTestCase):
    def setUp(self):
        self.env = JubaTestEnvironment()

    def test_node(self):
        self.env._node_records.append(('myhost', [10000]))
        self.assertEqual('myhost', self.env.get_node(0).get_host())
        self.assertEqual(10000, self.env.get_node(0).lease_port())

    def test_get_node(self):
        self.env._node_records.append(('myhost1', [10000]))
        self.env._node_records.append(('myhost2', [10000]))
        self.assertEqual('myhost1', self.env.get_node(0).get_host())
        self.assertEqual('myhost2', self.env.get_node(1).get_host())
        self.assertRaises(JubaSkipTest, self.env.get_node, 2)

class JubaNodeTest(JubaTestCase):
    def test_pool_1(self):
        n = JubaNode('localhost', range(10,11), None, '/tmp', [])

        port = n.lease_port()

        self.assertEqual(10, port)
        self.assertEqual(1, len(n._ports))
        self.assertEqual(0, len(n._free_ports))
        self.assertEqual(1, n.ports_used())

        n.free_port(port)

        self.assertEqual(1, len(n._ports))
        self.assertEqual(1, len(n._free_ports))
        self.assertEqual(0, n.ports_used())

    def test_pool_3(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])

        port1 = n.lease_port()
        port2 = n.lease_port()

        self.assertEqual(10000, port1)
        self.assertEqual(10001, port2)
        self.assertEqual(3, len(n._ports))
        self.assertEqual(1, len(n._free_ports))
        self.assertEqual(2, n.ports_used())

        n.free_port(port1)
        n.free_port(port2)

        self.assertEqual(3, len(n._ports))
        self.assertEqual(3, len(n._free_ports))
        self.assertEqual(0, n.ports_used())

        port3 = n.lease_port()

        self.assertEqual(10002, port3)

        port4 = n.lease_port()

        self.assertEqual(10000, port4)

    def test_pool_skip(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])

        port1 = n.lease_port()
        port2 = n.lease_port()
        port3 = n.lease_port()

        self.assertRaises(JubaSkipTest, n.lease_port)

    def test_pool_doublefree(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])

        port1 = n.lease_port()
        n.free_port(port1)

        self.assertRaises(JubaTestAssertionError, n.free_port, port1)

    def test_pool_nonmember(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])

        self.assertRaises(JubaTestAssertionError, n.free_port, 50000)

    def test_put_file(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])
        with tempfile.NamedTemporaryFile() as tmp:
            n.put_file('foo', tmp.name)
            self.assertEqual('foo', tmp.read())

    def test_put_file_delete_file(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])
        path = n.put_file('foo')
        self.assertTrue(os.path.isfile(path))
        with open(path, 'r') as f:
            self.assertEqual('foo', f.read())
        n.delete_file(path)
        self.assertFalse(os.path.isfile(path))

    def test_get_file(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])
        with tempfile.NamedTemporaryFile() as tmp1, tempfile.NamedTemporaryFile() as tmp2:
            tmp1.write('bar')
            tmp1.flush()
            n.get_file(tmp1.name, tmp2.name)
            self.assertEqual('bar', tmp2.read())

    def test_get_file_temp(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])
        contents_remote = n.get_file('/etc/hosts')
        with open('/etc/hosts', 'r') as f:
            contents_local= f.read()
        self.assertEqual(contents_local, contents_remote)

    def test_get_process(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])
        proc = n.get_process(['sleep', '100'])
        proc.start()
        time.sleep(1)
        proc.stop()
        self.assertEqual('', proc.stdout)

    def test_run_process(self):
        n = JubaNode('localhost', range(10000,10003), None, '/tmp', [])
        contents_remote = n.run_process(['cat', '/etc/hosts'])
        with open('/etc/hosts', 'r') as f:
            contents_local= f.read()
        self.assertEqual(contents_local, contents_remote)

class JubaRPCServerTest(JubaTestCase):
    def setUp(self):
        self.node = JubaNode('127.0.0.1', [12345], None, '/tmp', [])
        self.instance = JubaRPCServer(self.node, CLASSIFIER, [])
        self.stub_instance = JubaRPCServerStub(self.node)

    def test_start_fail(self):
        self.assertRaises(JubaTestFixtureFailedError, self.stub_instance.start)

    def test_get_client_fail(self):
        self.assertRaises(JubaTestAssertionError, self.instance.get_client, 'foo')

    def test_get_client_class(self):
        server = JubaRPCServer(self.node, CLASSIFIER, [])
        self.assertEqual(server.get_client_class(), jubatus.classifier.client.Classifier)

        server = JubaRPCServer(self.node, NEAREST_NEIGHBOR, [])
        self.assertEqual(server.get_client_class(), jubatus.nearest_neighbor.client.NearestNeighbor)

    def test_get_client_type(self):
        self.assertIsInstance(self.instance.get_client_type('Datum')(), jubatus.common.Datum)

    def test_types(self):
        self.assertIsInstance(self.instance.types.Datum(), jubatus.common.Datum)

    def test_get_host_port(self):
        (host, port) = self.instance.get_host_port()
        self.assertEqual('127.0.0.1', host)
        self.assertEqual(None, port) # port will not be allocated before calling start

    def test_log_fail(self):
        self.assertRaises(JubaTestAssertionError, self.instance.log)

    def test_flatten_options(self):
        opts = [('--opt1', 'yes'), ('--opt2', 100), ('--opt1', 'no')]
        expected = ['--opt1', 'yes', '--opt2', '100']
        self.assertEqual(expected, self.instance._flatten_options(opts))

class JubaRPCServerStub(JubaRPCServer):
    def __init__(self, node):
        super(JubaRPCServerStub, self).__init__(node, 'echo', [('option', 'yes')])

    def program(self):
        return 'echo'
