# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import time
import os

from .process import LocalSubprocess
from .exceptions import JubaTestException
from .logger import log

class RemoteProcessFailedError(JubaTestException):
    pass

class SyncRemoteProcess(object):
    """
    Provides a simple, synchronized remote process invocation and file transfer interface.
    """

    @classmethod
    def get_file(cls, from_host, from_file, to_file):
        cls._scp(from_host + ':' + from_file, os.path.abspath(to_file))

    @classmethod
    def put_file(cls, to_host, from_file, to_file):
        cls._scp(os.path.abspath(from_file), to_host + ':' + to_file)

    @classmethod
    def run(cls, host, args, envvars={}, timeout=None):
        process = LocalSubprocess(_RemoteUtil.ssh_cmdline(host, args, envvars))
        process.start()
        if timeout:
            for i in range(int(timeout)):
                if not process.is_running(): break
                time.sleep(1)
            else:
                process.stop()
                raise RemoteProcessFailedError('remote process timed out: {}'.format(str(args)))
        returncode = process.wait()
        if returncode != 0:
            raise RemoteProcessFailedError('remote process failed with status {0}: {1} (out: {2}, err: {3})'.format(returncode, args, process.stdout, process.stderr))
        return process.stdout

    @classmethod
    def _scp(cls, from_arg, to_arg):
        process = LocalSubprocess(_RemoteUtil.scp_cmdline(from_arg, to_arg))
        process.start()
        returncode = process.wait()
        if returncode != 0:
            raise RemoteProcessFailedError('SCP failed with status {}: {} -> {}'.format(returncode, from_arg, to_arg))

class AsyncRemoteProcess(LocalSubprocess):
    """
    Provides remote (over-SSH) process invocation intetface.
    """

    def __init__(self, host, args, envvars={}, timeout=None):
        """
        Prepares for process invocation.
        `host` can be an entry from ssh_config.
        """
        self.remote_host = host
        self.remote_args = args
        self.remote_envvars = envvars

        ssh_args = _RemoteUtil.ssh_jobcontrol_cmdline(host, args, envvars, timeout)
        super(AsyncRemoteProcess, self).__init__(ssh_args)

    def __del__(self):
        """
        Process should be stopped before destruction.
        """
        if self.is_running():
            log.warning('remote process is still running on %s! KILLing... %s', self.remote_host, self.remote_args)
            self.stop('KILL')

            # Wait for the remote process to be KILLed.
            # To avoid process to become defunct, we don't want to KILL the local ssh process.
            time.sleep(3)
        super(AsyncRemoteProcess, self).__del__()

    def wait(self):
        """
        Note: cannot acquire return code when running async process,
        as job-controlled SSH command line uses `wait` which always returns 0.
        """
        super(AsyncRemoteProcess, self).wait('\n')

    def stop(self, signal='TERM'):
        super(AsyncRemoteProcess, self).wait(signal.encode() + b'\n')

class _RemoteUtil(object):
    @classmethod
    def ssh_cmdline(cls, host, args, envvars):
        ssh_args = []
        for envvar in envvars:
            ssh_args += ['export', str(envvar) + '=' + str(envvars[envvar]), ';']
        ssh_args += args
        return ['ssh', '-q', host] + ssh_args

    @classmethod
    def ssh_jobcontrol_cmdline(cls, host, args, envvars, timeout=None):
        return cls.ssh_cmdline(host, args, envvars) + cls._ssh_jobcontrol_suffix(timeout)

    @classmethod
    def _ssh_jobcontrol_suffix(cls, timeout=None):
        """
        By default, remote processes receive SIGHUP when the SSH client is
        disconnected (i.e., the local `ssh` process is terminated).
        However, when Jubatus processes receive SIGHUP; they:
          - immediately be KILLed without closing resources
            including ZooKeeper connections (prior to Jubatus 0.6.1)
          - reload the log config and continue working (Jubatus 0.6.2 or later)
        ... both causing the following test cases to (possibly) fail.
        This suffix enables test cases to send any signal to the remote
        processes.  We can give the signal name via the standard input.
        """
        if timeout:
            timeout_args = ['-t', str(int(timeout))]
        else:
            timeout_args = []

        return [
                 '&', '{',
                       # when read failed (connection disconnect, timeout, etc.), always set KILL.
                       'read'] + timeout_args + ['_SIG', '||', '{', '_SIG=KILL', ';', 'echo', 'JUBATEST: Process timed out, KILLing', ';', '}', ';'
                       # if the read signal is not empty, send it to all the process whose Parent PID is the shell.
                       '[', '-z', '${_SIG}', ']', '||', 'pkill', '-${_SIG}', '-P$$', ';',
                       # wait for the subprocesses to complete.
                       'wait', ';'
                 '}', '>&2',
               ]

    @classmethod
    def scp_cmdline(cls, from_arg, to_arg):
        return ['scp', '-q', from_arg, to_arg]
