# -*- coding: utf-8 -*-

"""
Log parser for Jubatus servers/keepers
"""

import re
from datetime import datetime

from .exceptions import JubaTestAssertionError
from .logger import log

class Log:
    """
    Represents one log entry.
    """

    log_juba = re.compile('^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}),(\d{3})\s+(\d+)\s+([A-Z]+)\s+\[(.+?):(\d+)\] ')
    log_zk   = re.compile('^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}),(\d{3}):(\d+)\((0x[0-9a-f]+)\):ZOO_([A-Z]+)@(.+?)@(\d+): ')

    def __init__(self, node, line):
        """
        Creates new log entry for given line and node.
        """
        m = self.log_juba.match(line)
        if m:
            self.node = node
            self.type = 'jubatus'
            self.level = LogLevel.normalize(m.group(9))
            self.time = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6)), int(m.group(7)) * 1000)
            self.thread_id = int(m.group(8))
            self.source = m.group(10)
            self.source_line = m.group(11)
            self.message = self.log_juba.sub('', line)
            return
        m = self.log_zk.match(line)
        if m:
            self.node = node
            self.type = 'zookeeper'
            self.level = LogLevel.normalize(m.group(10))
            self.time = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6)), int(m.group(7)) * 1000)
            self.thread_id = int(m.group(8))
            self.handle = m.group(9)
            self.source = m.group(11)
            self.source_line = m.group(12)
            self.message = self.log_zk.sub('', line)
            return
        raise JubaTestAssertionError('invalid log format: %s' % line)

    def __repr__(self):
        # TODO refine
        return ("Log Type: %s\n" % self.type) + \
               ("Log Level: %s\n" % self.level) + \
               ("Log Time: %s\n" % self.time) + \
               ("Log Thread: %s\n" % self.thread_id) + \
               ("Log Source: %s\n" % self.source) + \
               ("Log Msg: %s\n" % self.message)

    @staticmethod
    def parse_logs(node, logs):
        """
        Parses the given logs in string format for given node.
        Returns list of Logs.
        """
        entries = []
        lines = logs.splitlines(False)
        while lines:
            line = lines.pop(0)
            while lines and not ((Log.log_juba.match(lines[0]) or Log.log_zk.match(lines[0]))):
                line += '\n' + lines.pop(0)
            entries += [Log(node, line)]
        return entries

class LogLevel:
    """
    Represents log levels.
    """

    FATAL = 'FATAL'
    ERROR = 'ERROR'
    WARN = 'WARN'
    INFO = 'INFO'
    DEBUG = 'DEBUG'

    levels = [FATAL, ERROR, WARN, INFO, DEBUG]

    @staticmethod
    def normalize(level):
        """
        Normalizes the given log level.
        """
        if level in LogLevel.levels:
            return level
        for l in LogLevel.levels:
            if l[0] == level:
                return l
        raise ValueError('invalid log level')

class LogFilter:
    """
    Fluent interface that filters log entries.
    """

    def __init__(self, logs):
        """
        Creates new filter for given list of Logs.
        """
        self.logs = logs

    def __iter__(self):
        """
        Iterates over all the logs.
        """
        return self.logs.__iter__()

    def type(self, arg):
        return LogFilter(filter(lambda l: l.type == arg, self.logs))

    def node(self, arg):
        return LogFilter(filter(lambda l: l.node == arg, self.logs))

    def level(self, arg):
        return LogFilter(filter(lambda l: l.level == arg, self.logs))

    def time_range(self, begin, end):
        return LogFilter(filter(lambda l: begin <= l.time and l.time <= end, self.logs))

    def message(self, pattern):
        return LogFilter(filter(lambda l: re.search(pattern, l.message), self.logs))

    def consume(self, log):
        return LogFilter(self.logs[self.logs.index(log)+1:])

    def get(self):
        return self.logs

    def __str__(self):
        return '\n'.join(map(lambda x: str(x), self.logs))
