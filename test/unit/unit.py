# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import time
import unittest

from jubatest import *
from jubatest.unit import get_suite

class JubaTestCaseTest(JubaTestCase):
    class TestCaseStub(JubaTestCase):
        def runTest(self):
            pass

    def test_assertRunsWithin(self):
        t = self.TestCaseStub()
        t.assertRunsWithin(2, time.sleep, 1)

    def test_record(self):
        t = self.TestCaseStub()
        t.attach_record("mydata")
        self.assertEquals("mydata", t.get_record())

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
