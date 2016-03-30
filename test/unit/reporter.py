# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from xml.dom.minidom import *
import re

from jubatest import *
from jubatest.unit import JubaTestCase
from jubatest.reporter import JubaTestXunitReporter

class JubaTestXunitReporterTest(JubaTestCase):
    def assertToXUnitResult(self, expected, result):
        reporter = JubaTestXunitReporter()
        canonicalizer = re.compile('>[\s\n]+<')
        normalized_expected = canonicalizer.sub('><', xml.dom.minidom.parseString(expected).toprettyxml(indent=''))
        normalized_actual   = canonicalizer.sub('><', xml.dom.minidom.parseString(reporter.create_report(result)).toprettyxml(indent=''))
        self.assertEqual(normalized_expected, normalized_actual)

    def test_to_xunit_empty(self):
        expected = """<?xml version="1.0" ?>
        <testsuite errors="0" failures="0" name="jubatest" skip="0" tests="0" />
        """
        result = TestResultStub()
        self.assertToXUnitResult(expected, result)

    def test_to_xunit_success(self):
        expected = """<?xml version="1.0" ?>
        <testsuite errors="0" failures="0" name="jubatest" skip="0" tests="1">
        <testcase classname="test1.test2" name="MyTest" time="1.2" />
        </testsuite>
        """
        result = TestResultStub()
        result.successes.append(TestStub())
        result.testsRun += 1
        self.assertToXUnitResult(expected, result)

    def test_to_xunit_failure(self):
        expected = """<?xml version="1.0" ?>
        <testsuite errors="0" failures="1" name="jubatest" skip="0" tests="1">
        <testcase classname="test1.test2" name="MyTest" time="1.2">
        <failure>msg</failure>
        </testcase>
        </testsuite>
        """
        result = TestResultStub()
        result.failures.append((TestStub(), 'msg'))
        result.testsRun += 1
        self.assertToXUnitResult(expected, result)

    def test_to_xunit_error(self):
        expected = """<?xml version="1.0" ?>
        <testsuite errors="1" failures="0" name="jubatest" skip="0" tests="1">
        <testcase classname="test1.test2" name="MyTest" time="1.2">
        <error>msg</error>
        </testcase>
        </testsuite>
        """
        result = TestResultStub()
        result.errors.append((TestStub(), 'msg'))
        result.testsRun += 1
        self.assertToXUnitResult(expected, result)

    def test_to_xunit_skip(self):
        expected = """<?xml version="1.0" ?>
        <testsuite errors="0" failures="0" name="jubatest" skip="1" tests="1">
        <testcase classname="test1.test2" name="MyTest" time="1.2">
        <skipped>msg</skipped>
        </testcase>
        </testsuite>
        """
        result = TestResultStub()
        result.skipped.append((TestStub(), 'msg'))
        result.testsRun += 1
        self.assertToXUnitResult(expected, result)

class TestResultStub(object):
    def __init__(self):
        self.testsRun = 0
        self.successes = []
        self.errors = []
        self.failures = []
        self.skipped = []

class TestStub(object):
    def __init__(self, *args, **kwds):
        self.timeTaken = 1.2
        self._record = {}
        self.attachLogs = False

    def id(self):
        return "test1.test2.MyTest"

    def test(self):
        pass
