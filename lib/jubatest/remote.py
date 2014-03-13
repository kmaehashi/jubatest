# -*- coding: utf-8 -*-

import time
import os

from .process import LocalSubprocess
from .exceptions import JubaTestException
from .logger import log

# ssh command must be invoked with quiet mode
_ssh_command = ['ssh', '-q']
_scp_command = ['scp', '-q']

# ssh sends HUP to remote process on receiveing TERM, so wrap it as the signal given via stdin
_command_wait_suffix = [ '&', '{', 'read', 'SIG', ';', 'pkill', '-${SIG:-KILL}', '-P$$', ';', 'wait', ';', '}', '&>', '/dev/null' ]

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
        args = _scp_command + [from_host + ':' + from_file, os.path.abspath(to_file)]
        cls._run(args)

    @classmethod
    def put_file(cls, to_host, from_file, to_file):
        args = _scp_command + [os.path.abspath(from_file), to_host + ':' + to_file]
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
        self.remote_host = host
        self.remote_args = args
        self.remote_envvars = envvars

        ssh_args = _ssh_command + [host]
        for envvar in envvars:
            ssh_args += ['export', str(envvar) + '=' + str(envvars[envvar]), ';']
        ssh_args += args + _command_wait_suffix
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
        raise NotImplementedError('cannot wait for remote processes')

    def stop(self, signal='TERM'):
        super(AsyncRemoteProcess, self).wait(signal + '\n')
