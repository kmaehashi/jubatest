# -*- coding: utf-8 -*-

import time
import tempfile

from jubatest import *

from jubatest.remote import SyncRemoteProcess, AsyncRemoteProcess, RemoteProcessFailedError

class SyncRemoteProcessTest(JubaTestCase):
    def test_run(self):
        result = SyncRemoteProcess.run('localhost', ['/bin/echo', '-n', 'foo'])
        self.assertEqual('foo', result)

    def test_run_envvar(self):
        result = SyncRemoteProcess.run('localhost', ['/bin/echo', '-n', '${PARAM}'], {'PARAM': 'bar'})
        self.assertEquals('bar', result)

    def test_run_timeout(self):
        result = SyncRemoteProcess.run('localhost', ['/bin/echo', '-n', 'baz'], {}, 5)
        self.assertEquals('baz', result)

    def test_run_timeout_fail(self):
        result = SyncRemoteProcess.run('localhost', ['sleep', '5'], {}, 3)
        self.assertEquals('baz', result)

    def test_run_fail(self):
        self.assertRaises(RemoteProcessFailedError, SyncRemoteProcess.run, 'localhost', ['/'])

    def test_get_file(self):
        with tempfile.NamedTemporaryFile() as tmp:
            SyncRemoteProcess.get_file('localhost', '/etc/hosts', tmp.name)
            with open('/etc/hosts', 'r') as expected_file:
                self.assertEqual(expected_file.read(), tmp.read())

    def test_get_file_remote_fail(self):
        self.assertRaises(RemoteProcessFailedError, SyncRemoteProcess.get_file, 'localhost', '/no-such-file', '/tmp')

    def test_get_file_local_fail(self):
        self.assertRaises(RemoteProcessFailedError, SyncRemoteProcess.get_file, 'localhost', '/etc/hosts', '/no-such-dir/no-such-file')

    def test_put_file(self):
        with tempfile.NamedTemporaryFile() as tmp1, tempfile.NamedTemporaryFile() as tmp2:
            tmp1.write('foo')
            tmp1.flush()
            SyncRemoteProcess.put_file('localhost', tmp1.name, tmp2.name)
            self.assertEqual('foo', tmp2.read())

    def test_put_file_local_fail(self):
        self.assertRaises(RemoteProcessFailedError, SyncRemoteProcess.put_file, 'localhost', '/no-such-file', '/tmp')

    def test_put_file_remote_fail(self):
        self.assertRaises(RemoteProcessFailedError, SyncRemoteProcess.put_file, 'localhost', '/etc/hosts', '/no-such-dir/no-such-file')

class AsyncRemoteProcessTest(JubaTestCase):
    def test_run(self):
        p = AsyncRemoteProcess('localhost', ['/bin/echo', '-n', 'foo'], [])
        p.start()
        for i in range(20): # expecting this command to complete in two second
            time.sleep(0.1)
        p.stop()
        self.assertFalse(p.is_running())
        self.assertEqual('foo', p.stdout)

    def test_destructor(self):
        p = AsyncRemoteProcess('localhost', ['sleep', '120'], [])
        p.start()
        rawp = p._process
        p = None # run destructor
        time.sleep(1)
        self.assertIsNotNone(rawp.poll())

    def test_stop(self):
        def _test():
            p = AsyncRemoteProcess('localhost', ['sleep', '120'], [])
            p.start()
            time.sleep(3)
            p.stop()
        self.assertRunsWithin(10, _test)

    def test_timeout(self):
        p = AsyncRemoteProcess('localhost', ['sleep', '120'], [], 1)
        p.start()
        time.sleep(5)
        self.assertFalse(p.is_running())
