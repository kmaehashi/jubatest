# -*- coding: utf-8 -*-

"""
Unittest framework
"""

import unittest
from datetime import datetime
import time

from .logger import log
from .exceptions import JubaTestException

class JubaTestFixtureFailedError(JubaTestException):
    pass

class JubaTestCase(unittest.TestCase):
    def __init__(self, *args, **kwds):
        self._record = None
        self.attachLogs = False
        super(JubaTestCase, self).__init__(*args, **kwds)

    def assertRunsWithin(self, timeout, func, *args, **kwds):
        time_begin = datetime.now()
        result = func(*args, **kwds)
        delta = (datetime.now() - time_begin).seconds
        self.assertGreaterEqual(timeout, delta, 'expected to run in %f seconds, but it took %f seconds' % (timeout, delta))
        return (result, timeout - delta)

    def attach_record(self, record):
        self._record = record

    def get_record(self):
        return self._record

class JubaSkipTest(unittest.SkipTest):
    pass

def get_loader(e):
    class JubaTestLoaderBoundToEnv(_JubaTestLoader):
        env = e
    return JubaTestLoaderBoundToEnv

def get_suite(e):
    class JubaTestSuiteBoundToEnv(_JubaTestSuite):
        env = e
    return JubaTestSuiteBoundToEnv

def get_runner(e):
    class JubaTestRunnerBoundToEnv(_JubaTestRunner):
        env = e
    return JubaTestRunnerBoundToEnv

def get_result(e):
    class JubaTestResultBoundToEnv(_JubaTestResult):
        env = e
    return JubaTestResultBoundToEnv

class _JubaTestRunner(unittest.TextTestRunner):
    class DevNull(object):
        def write(self, *args, **kwds):
            pass

    def __init__(self, *args, **kwds):
        unittest.installHandler()
        super(_JubaTestRunner, self).__init__(stream=self.DevNull(), resultclass=get_result(self.env), *args, **kwds)

class _JubaTestResult(unittest.TestResult):
    def __init__(self, *args, **kwds):
        self.successes = []
        super(_JubaTestResult, self).__init__(*args, **kwds)

    def startTest(self, test):
        """
        Record the start time.
        """
        log.info('test started: %s', test)
        self._timer = time.time()
        super(_JubaTestResult, self).startTest(test)

    def stopTest(self, test):
        """
        Record the time taken to run the test.
        """
        log.info('test stopped: %s', test)
        test.timeTaken = time.time() - self._timer
        super(_JubaTestResult, self).stopTest(test)

    def addSuccess(self, test):
        """
        unittest.TestResult does not record success tests, but we need them.
        """
        self.successes.append(test)
        super(_JubaTestResult, self).addSuccess(test)

    def addError(self, test, err):
        test.attachLogs = True
        super(_JubaTestResult, self).addError(test, err)

    def addFailure(self, test, err):
        test.attachLogs = True
        super(_JubaTestResult, self).addFailure(test, err)

    def addUnexpectedSuccess(self, test):
        test.attachLogs = True
        super(_JubaTestResult, self).addUnexpectedSuccess(test, err)

    def stop(self):
        log.warn('stopping test!')
        super(_JubaTestResult, self).stop()

class _JubaTestLoader(unittest.TestLoader):
    """
    Test classes inheriting JubaTestCase class may have a classmethod called
    `generateTests`, which takes 1 argument (JubaTestEnvironment instance).
    `generateTests` method is used to generate test cases at run-time.
    `generateTests` will be called when loading test cases, so you shouldn't
    do any test fixture related things in this method.
    """
    def loadTestsFromTestCase(self, testCaseClass):
        env = self.env
        if hasattr(testCaseClass, 'generateTests'):
            generatedTests = testCaseClass.generateTests(env)
            for generatedTest in generatedTests:
                func = generatedTest[0]
                args = generatedTest[1:]
                name = '%s:%s%s' % (self.testMethodPrefix, func.__name__, str(args))
                setattr(testCaseClass, name, lambda s, func=func, args=args: func(s, *args))
        loaded_suite = super(_JubaTestLoader, self).loadTestsFromTestCase(testCaseClass)
        return loaded_suite

class _JubaTestSuite(unittest.TestSuite):
    """
    Test classes inheriting JubaTestCase class may have a classmethod called
    `setUpCluster`, which takes 1 argument (JubaTestEnvironment instance).
    `setUpCluster` method is used to configure the cluster fixture to satisfy
    the pre-conditions for the test case.
    `setUpCluster` will be called just before `setUpClass` method.
    """
    def run(self, *args, **kwds):
        env = self.env
        def _wrapSetUpClassMethod(setUpClassMethod):
            @classmethod
            def setUpClass(cls):
                env.initialize_test_class(cls)
                if getattr(cls, 'setUpCluster', None):
                    cls.setUpCluster(env)
                if setUpClassMethod:
                    setUpClassMethod()
            return setUpClass
        def _wrapTearDownClassMethod(tearDownClassMethod):
            @classmethod
            def tearDownClass(cls):
                try:
                    if getattr(cls, 'tearDownCluster', None):
                        cls.tearDownCluster(env)
                    if tearDownClassMethod:
                        tearDownClassMethod()
                finally:
                    env.finalize_test_class(cls)
            return tearDownClass
        for test in self:
            if issubclass(test.__class__, JubaTestCase):
                wrapped_flag = '__jubatest_wrapped'
                if not getattr(test.__class__, wrapped_flag, None):
                    # add flag
                    setattr(test.__class__, wrapped_flag, True)
                    # wrap setUpClass
                    setUpClassMethod = getattr(test.__class__, 'setUpClass', None)
                    setattr(test.__class__, 'setUpClass', _wrapSetUpClassMethod(setUpClassMethod))
                    # wrap tearDownClass
                    tearDownClassMethod = getattr(test.__class__, 'tearDownClass', None)
                    setattr(test.__class__, 'tearDownClass', _wrapTearDownClassMethod(tearDownClassMethod))
                # add cleanUp
                test.addCleanup(env.finalize_test_case, test)
        super(_JubaTestSuite, self).run(*args, **kwds)
