#!/usr/bin/env python

import os
import re

import msgpackrpc

from jubatest import *
from jubatest.log import LogLevel

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
            self.assertIsNotNone(re.match('\d+\.\d+\.\d+\.\d+_\d+', server1_id), server1_id)

            # query server
            d = server1.types.datum([('foo', 'bar')],[])
            self.assertEqual(1, cli.train('', [('label', d)]))

            # save
            self.assertEqual(True, cli.save('', 'baz'))

            # get model file
            model_data = server1.get_saved_model('baz')
            self.assertNotEqual(0, len(model_data))

        self.assertRaises(msgpackrpc.error.RPCError, cli.train, '', [('label', d)])

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

        # start server, test, and stop server
        with server1, keeper1 as cli:
            self.assertTrue(keeper1.is_running())
            self.assertEqual(keeper1.port, keeper1.get_host_port()[1])
            self.assertTrue(keeper1.is_ready())

            # program
            self.assertTrue('jubaclassifier_keeper', keeper1.program())

            # count servers in the cluster
            self.assertEqual(1, len(keeper1.get_cluster_members(cluster)))

            # query keeper
            d = keeper1.types.datum([('foo', 'bar')],[])
            self.assertEqual(1, cli.train(cluster.name, [('label', d)]))

        self.assertRaises(msgpackrpc.error.RPCError, cli.train, cluster.name, [('label', d)])

        # parse log
        logs = keeper1.log().level(LogLevel.INFO).message('start listening at port').get()
        self.assertEqual(1, len(logs))
