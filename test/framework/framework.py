#!/usr/bin/env python

import os
import re

import msgpackrpc

from jubatest import *
from jubatest.log import LogLevel
from jubatest.exceptions import JubaTestAssertionError

class FrameworkTest(JubaTestCase):
    @classmethod
    def setUpCluster(cls, env):
        cls.env = env

    def test_standalone(self):
        # node
        node0 = self.env.get_node(0)

        # test server
        server1 = self.env.server_standalone(node0, CLASSIFIER, default_config(CLASSIFIER))

        # start server, test, and stop server
        with server1 as cli:
            self.assertTrue(server1.is_running())
            self.assertEqual(server1.port, server1.get_host_port()[1])
            self.assertTrue(server1.is_ready())

            # program
            self.assertTrue('jubaclassifier', server1.program())

            # get server ID
            server1_id = server1.get_id()
            self.assertIsNotNone(re.match(r'\d+\.\d+\.\d+\.\d+_\d+', server1_id), server1_id)

            # query server
            d = server1.types.Datum({'foo': 'bar'})
            self.assertEqual(1, cli.train([('label', d)]))

            # save
            self.assertEqual(True, cli.save('baz'))

            # get model file
            model_data = server1.get_saved_model('baz')
            self.assertNotEqual(0, len(model_data))

        self.assertRaises(msgpackrpc.error.RPCError, cli.train, [('label', d)])

        # parse log
        logs = server1.log().level(LogLevel.INFO).message('start listening at port').get()
        self.assertEqual(1, len(logs))

    def test_distributed(self):
        # node
        node0 = self.env.get_node(0)

        # test cluster
        cluster = self.env.cluster(CLASSIFIER, default_config(CLASSIFIER))

        # test server and keeper
        server1 = self.env.server(node0, cluster)
        keeper1 = self.env.keeper(node0, CLASSIFIER)

        # calling get_client for servers not started yet should fail
        self.assertRaises(JubaTestAssertionError, server1.get_client)
        self.assertRaises(JubaTestAssertionError, keeper1.get_client)

        # start server and keeper
        keeper1.start()
        server1.start()
        keeper1.wait_for_servers(server1)

        self.assertTrue(keeper1.is_running())
        self.assertEqual(keeper1.port, keeper1.get_host_port()[1])
        self.assertTrue(keeper1.is_ready())

        # program
        self.assertTrue('jubaclassifier_proxy', keeper1.program())

        # count servers in the cluster
        self.assertEqual(1, len(keeper1.get_cluster_members(cluster)))

        # query keeper
        d = keeper1.types.Datum({'foo': 'bar'})
        cli = keeper1.get_client(cluster.name)
        self.assertEqual(1, cli.train([('label', d)]))

        # stop servers and keepers
        server1.stop()
        keeper1.stop()

        self.assertRaises(msgpackrpc.error.RPCError, cli.train, [('label', d)])

        # parse log
        logs = keeper1.log().level(LogLevel.INFO).message('start listening at port').get()
        self.assertEqual(1, len(logs))

    def test_stop_kill(self):
        # node
        node0 = self.env.get_node(0)

        # test server
        server1 = self.env.server_standalone(node0, CLASSIFIER, default_config(CLASSIFIER))

        # start and stop the server
        server1.start()
        server1.stop()

        # parse log
        logs = server1.log().level(LogLevel.INFO).message('stopping RPC server').get()
        self.assertEqual(1, len(logs))

        # start and stop the server
        server1.start()
        server1.stop()

        # start and kill the server
        server1.start()
        server1.kill()

        # parse log
        logs = server1.log().level(LogLevel.INFO).message('stopping RPC server').get()
        self.assertEqual(0, len(logs))
