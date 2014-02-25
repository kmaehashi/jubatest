# -*- coding: utf-8 -*-

"""
Provides local process management interface.
"""

import os
import errno
import time
from subprocess import Popen, PIPE

from .unit import JubaTestFixtureFailedError
from .logger import log

class LocalSubprocess(object):
    def __init__(self, args, env=None):
        """
        Prepares for process invocation.
        """
        self.args = args
        if env:
            self.env = env
        else:
            self.env = os.environ
        self.stdout = None
        self.stderr = None
        self._process = None
        self._started = False

    def __del__(self):
        """
        Process should be stopped before destruction.
        """
        p = self._process
        if p is not None and p.poll() is None:
            log.warning('process is still running! KILLing... %s', self.args)
            p.kill()

    def start(self):
        """
        Invokes process.
        """
        if self._started:
            raise JubaTestFixtureFailedError('cannot start again using same instance')
        self._started = True
        log.debug('starting process: %s', self.args)
        self._process = Popen(self.args, env=self.env, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        log.debug('started process: %s', self.args)

    def wait(self, stdin=None):
        log.debug('waiting for process to complete: %s', self.args)
        (self.stdout, self.stderr) = self._process.communicate(stdin)
        log.debug('process completed: %s', self.args)
        return self._process.returncode

    def stop(self, kill=False):
        """
        Stops (usually TERM, but KILL at your will) the invoked process.
        """
        if not self._started or not self._process:
            raise JubaTestFixtureFailedError('this instance has not been started yet')

        try:
            if kill:
                log.debug('KILLing process')
                self._process.kill()
            else:
                log.debug('terminating process')
                self._process.terminate()
        except OSError as e:
            if e.errno != errno.ESRCH: # "No such process"
                raise e
            # may be a race between poll and signal; just ignore
            log.debug('race between poll and signal detected')
        (self.stdout, self.stderr) = self._process.communicate()
        return True

    def is_running(self):
        """
        Returns whether the process we invoked is still running.
        """
        if self._process.poll() is None:
            return True
        return False
