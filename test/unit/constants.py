# -*- coding: utf-8 -*-

import time

from jubatest import *
from jubatest.unit import JubaTestFixtureFailedError

class DefaultConfigTest(JubaTestCase):
    def test_sleep(self):
        begin = time.time()
        sleep(1) # from jubatest.constants
        timeTaken = time.time() - begin
        self.assertAlmostEqual(1.0, timeTaken, places=2)

    def test_default_config_classifier_immutable(self):
        cfg1 = default_config(CLASSIFIER)
        cfg1['method'] = 'none'
        cfg2 = default_config(CLASSIFIER)
        self.assertNotEqual(cfg1['method'], cfg2['method'])

    def test_default_config_recommender(self):
        self.assertIsNotNone(default_config(RECOMMENDER))

    def test_default_config_fail(self):
        self.assertRaises(JubaTestFixtureFailedError, default_config, 'fail')
