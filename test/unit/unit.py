# -*- coding: utf-8 -*-

import time
import unittest

from jubatest import *
from jubatest.unit import JubaTestResult, get_suite

class JubaTestResultTest(JubaTestCase):
    def test_startTest_stopTest(self):
        t = TestStub()
        r = JubaTestResult()
        r.startTest(t)
        time.sleep(1)
        r.stopTest(t)
        self.assertAlmostEqual(1.0, t.timeTaken, places=2)

    def test_addSuccess(self):
        t = TestStub()
        r = JubaTestResult()
        r.startTest(t)
        r.stopTest(t)
        r.addSuccess(t)
        self.assertEqual(1, len(r.successes))
        self.assertEqual(t, r.successes[0])

    def test_get_suite(self):
        self.assertTrue(get_suite(None), unittest.TestSuite)

class TestStub(object):
    def run(*args, **kwds):
        pass

class JubaTestLoaderTest(JubaTestCase):
    @classmethod
    def generateTests(cls, env):
        for i in (1, 2, 3, True, False):
            yield cls.check_is_number_or_bool, i
        for (x, y) in [(2, 4), (3, 9), (4, 16)]:
            yield cls.check_pow, x, y

    def setUp(self):
        if not hasattr(self, 'test_is_ready') or not self.test_is_ready:
            self.test_is_ready = True

    def tearDown(self):
        self.test_is_ready = False

    def check_is_number_or_bool(self, v):
        # make sure that setUp is called before running generated tests
        self.assertTrue(self.test_is_ready)

        self.assertTrue(isinstance(v, int) or isinstance(v, bool))

    def check_pow(self, x, y):
        self.assertEquals(y, x*x)
