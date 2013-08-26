# -*- coding: utf-8 -*-

import time

from .process import LocalSubprocess
from .exceptions import JubaTestException

# ssh command must be invoked with quiet mode
_ssh_command = ['ssh', '-q']
_scp_command = ['scp', '-q']

# ssh sends HUP to remote process on receiveing TERM, so wrap it as TERM
_command_wait_suffix = [ '&', '{', 'read', ';', 'pkill', '-TERM', '-P$$', ';', 'wait', '}', '&>', '/dev/null' ]

class SyncRemoteProcess(object):
    """
    Provides a simple, synchronized remote process invocation and file transfer interface.
    """

    @classmethod
    def run(cls, host, args, envvars={}):
        ssh_args = _ssh_command + [host]
        for envvar in envvars:
            ssh_args += ['export', str(envvar) + '=' + str(envvars[envvar]), ';']
        ssh_args += args
        return cls._run(ssh_args)

    @classmethod
    def get_file(cls, from_host, from_file, to_file):
        args = _scp_command + [from_host + ':' + from_file, to_file]
        cls._run(args)

    @classmethod
    def put_file(cls, to_host, from_file, to_file):
        args = _scp_command + [from_file, to_host + ':' + to_file]
        cls._run(args)

    @classmethod
    def _run(cls, args):
        process = LocalSubprocess(args)
        process.start()
        returncode = process.wait()
        if returncode != 0:
            raise RemoteProcessFailedError('remote process failed with status %d: %s' % (returncode, str(args)))
        return process.stdout

class RemoteProcessFailedError(JubaTestException):
    pass

class AsyncRemoteProcess(LocalSubprocess):
    """
    Provides remote (over-SSH) process invocation intetface.
    """

    def __init__(self, host, args, envvars):
        """
        Prepares for process invocation.
        `host` can be an entry from ssh_config.
        """

        ssh_args = _ssh_command + [host]
        for envvar in envvars:
            ssh_args += ['export', str(envvar) + '=' + str(envvars[envvar]), ';']
        ssh_args += args + _command_wait_suffix
        super(AsyncRemoteProcess, self).__init__(ssh_args)

    def wait(self):
        raise NotImplementedError('cannot wait for async processes')

    def stop(self):
        super(AsyncRemoteProcess, self).wait('\n')
