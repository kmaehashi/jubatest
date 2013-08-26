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
