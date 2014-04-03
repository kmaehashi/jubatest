#!/usr/bin/env python

from jubatest import *
from jubatest.log import LogLevel

class TestBase(object):
    def do_test(self):
        cli = self.target.get_client(self.name)

        # query server and check result
        d = self.target.types.Datum({'foo': 'bar'})
        self.assertEqual(1, cli.train([('label', d)]))

        self._stop()

        # check log
        logs = self.target.log().level(LogLevel.INFO).message('start listening at port').get()
        self.assertEqual(1, len(logs))

    @classmethod
    def setUpCluster(cls, env):
        cls.env = env

    @classmethod
    def generateTests(cls, env):
        for (key,config) in get_configs(CLASSIFIER).items():
            yield cls.config_test, key, config

    def config_test(self, key, config):
        self._start(config)
        try:
            self.do_test()
        except:
            self._stop()
            raise

class StandaloneUseCase(JubaTestCase, TestBase):
    def _start(self, config):
        self.name = ''
        self.node0 = self.env.get_node(0)
        self.server0 = self.env.server_standalone(self.node0, CLASSIFIER, config)
        self.target = self.server0
        self.server0.start()

    def _stop(self):
        self.server0.stop()

class DistributedUseCase(JubaTestCase, TestBase):
    def _start(self, config):
        self.node0 = self.env.get_node(0)
        self.cluster = self.env.cluster(CLASSIFIER, config)
        self.server0 = self.env.server(self.node0, self.cluster)
        self.keeper0 = self.env.keeper(self.node0, CLASSIFIER)
        self.target = self.keeper0
        self.name = self.cluster.name

        self.server0.start()
        self.keeper0.start()

    def _stop(self):
        self.keeper0.stop()
        self.server0.stop()
