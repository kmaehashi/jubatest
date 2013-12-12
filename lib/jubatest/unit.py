# -*- coding: utf-8 -*-

"""
Unittest framework
"""

import unittest
from datetime import datetime
import time

from .logger import log
from .exceptions import JubaTestException

class _DevNull(object):
    def write(self, *args, **kwds):
        pass

class JubaTestFixtureFailedError(JubaTestException):
    pass

class JubaTestCase(unittest.TestCase):
    def __init__(self, *args, **kwds):
        self._record = None
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

class JubaTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwds):
        unittest.installHandler()
        super(JubaTestRunner, self).__init__(stream=_DevNull(), resultclass=JubaTestResult, *args, **kwds)

class JubaSkipTest(unittest.SkipTest):
    pass

class JubaTestResult(unittest.TestResult):
    def __init__(self, *args, **kwds):
        self.successes = []
        super(JubaTestResult, self).__init__(*args, **kwds)

    def startTest(self, test):
        """
        Record the start time.
        """
        log.info('test started: %s', test)
        self._timer = time.time()
        super(JubaTestResult, self).startTest(test)

    def stopTest(self, test):
        """
        Record the time taken to run the test.
        """
        log.info('test stopped: %s', test)
        test.timeTaken = time.time() - self._timer
        super(JubaTestResult, self).stopTest(test)

    def addSuccess(self, test):
        """
        unittest.TestResult does not record success tests, but we need them.
        """
        self.successes.append(test)
        super(JubaTestResult, self).addSuccess(test)

    def stop(self):
        log.warn('stopping test!')
        super(JubaTestResult, self).stop()

def get_loader(env):
    """
    Bind the global test environment to the test loader class and return it.
    """

    class JubaTestLoader(unittest.TestLoader):
        """
        Test classes inheriting JubaTestCase class may have a classmethod called
        `generateTests`, which takes 1 argument (JubaTestEnvironment instance).
        `generateTests` method is used to generate test cases at run-time.
        `generateTests` will be called when loading test cases, so you shouldn't
        do any test fixture related things in this method.
        """
        def loadTestsFromTestCase(self, testCaseClass):
            if hasattr(testCaseClass, 'generateTests'):
                generatedTests = testCaseClass.generateTests(env)
                for generatedTest in generatedTests:
                    func = generatedTest[0]
                    args = generatedTest[1:]
                    name = '%s:%s%s' % (self.testMethodPrefix, func.__name__, str(args))
                    setattr(testCaseClass, name, lambda s, func=func, args=args: func(s, *args))
            loaded_suite = super(JubaTestLoader, self).loadTestsFromTestCase(testCaseClass)
            return loaded_suite
    return JubaTestLoader

def get_suite(env):
    """
    Bind the global test environment to the test suite class and return it.
    """

    class JubaTestSuite(unittest.TestSuite):
        """
        Test classes inheriting JubaTestCase class may have a classmethod called
        `setUpCluster`, which takes 1 argument (JubaTestEnvironment instance).
        `setUpCluster` method is used to configure the cluster fixture to satisfy
        the pre-conditions for the test case.
        `setUpCluster` will be called just after `setUpClass` method.
        """
        def run(self, *args, **kwds):
            def _wrapSetUpClassMethod(setUpClassMethod):
                @classmethod
                def setUpClass(cls):
                    if getattr(cls, 'setUpCluster', None):
                        cls.setUpCluster(env)
                    if setUpClassMethod:
                        setUpClassMethod()
                return setUpClass
            for test in self:
                if issubclass(test.__class__, JubaTestCase):
                    # avoid double-wrapping the same class
                    if not getattr(test.__class__, 'setUpClass_wrapped', None):
                        setUpClassMethod = getattr(test.__class__, 'setUpClass', None)
                        setattr(test.__class__, 'setUpClass', _wrapSetUpClassMethod(setUpClassMethod))
                        setattr(test.__class__, 'setUpClass_wrapped', True)
            super(JubaTestSuite, self).run(*args, **kwds)
    return JubaTestSuite
