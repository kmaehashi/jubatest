# -*- coding: utf-8 -*-

import time

from jubatest import *
from jubatest.process import LocalSubprocess
from jubatest.unit import JubaTestFixtureFailedError

class LocalSubprocessTest(JubaTestCase):
    def test_start_stdout(self):
        p = LocalSubprocess(['echo', '-n', 'foo'])
        p.start()
        for i in range(10): # expecting this command to complete in a second
            time.sleep(0.1)
            if not p.is_running():
                break
        p.wait()
        self.assertEqual('foo', p.stdout)
        self.assertFalse(p.is_running())

    def test_start_again_fail(self):
        p = LocalSubprocess(['echo', '-n', 'foo'])
        p.start()
        p.stop(True)
        self.assertRaises(JubaTestFixtureFailedError, p.start)

    def test_stop(self):
        p = LocalSubprocess(['sleep', '100'])
        p.start()
        time.sleep(0.5)
        self.assertTrue(p.stop())

    def test_stop_before_start_fail(self):
        p = LocalSubprocess(['echo', '-n', 'foo'])
        self.assertRaises(JubaTestFixtureFailedError, p.stop)

    def test_wait(self):
        p = LocalSubprocess(['sleep', '1'])
        p.start()
        self.assertIsNotNone(p.wait())

    def test_is_running(self):
        p = LocalSubprocess(['sleep', '100'])
        p.start()
        self.assertTrue(p.is_running())
        time.sleep(0.5)
        self.assertTrue(p.stop(True))
        time.sleep(0.5)
        self.assertFalse(p.is_running())
