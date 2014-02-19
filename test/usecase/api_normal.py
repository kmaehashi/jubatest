#!/usr/bin/env python

from jubatest import *
from jubatest.log import LogLevel

class TestBase(object):
    def test(self):
        self._start()

        cli = self.target.get_client(self.name)

        # query server and check result
        d = self.target.types.Datum({'foo': 'bar'})
        self.assertEqual(1, cli.train([('label', d)]))

        self._stop()

        # check log
        logs = self.target.log().level(LogLevel.INFO).message('start listening at port').get()
        self.assertEqual(1, len(logs))

class StandaloneUseCase(JubaTestCase, TestBase):
    @classmethod
    def setUpCluster(cls, env):
        cls.node0 = env.get_node(0)
        cls.server0 = env.server_standalone(cls.node0, CLASSIFIER, default_config(CLASSIFIER))
        cls.target = cls.server0
        cls.name = ''

    def _start(self):
        self.server0.start()

    def _stop(self):
        self.server0.stop()

class DistributedUseCase(JubaTestCase, TestBase):
    @classmethod
    def setUpCluster(cls, env):
        cls.node0 = env.get_node(0)
        cls.cluster = env.cluster(CLASSIFIER, default_config(CLASSIFIER))
        cls.server0 = env.server(cls.node0, cls.cluster)
        cls.keeper0 = env.keeper(cls.node0, CLASSIFIER)
        cls.target = cls.keeper0
        cls.name = cls.cluster.name

    def _start(self):
        self.server0.start()
        self.keeper0.start()

    def _stop(self):
        self.keeper0.stop()
        self.server0.stop()
