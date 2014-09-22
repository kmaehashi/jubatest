#!/usr/bin/env python

from datetime import datetime, timedelta

from jubatest import *
from jubatest.log import Log, LogLevel, LogFilter
from jubatest.exceptions import JubaTestAssertionError

class LogTest(JubaTestCase):
    def test_init_jubalog_all(self):
        log = Log('localhost', '2014-05-16 13:58:52,905 28460 INFO  [server_util.cpp:217] starting jubaclassifier 0.4.3 RPC server at 192.168.122.211:9199')
        self.assertEqual('jubatus', log.type)
        self.assertEqual(LogLevel.INFO, log.level)
        self.assertEqual(datetime(2014, 5, 16, 13, 58, 52, 905000), log.time)
        self.assertEqual(28460, log.thread_id)
        self.assertEqual('server_util.cpp', log.source)
        self.assertEqual('217', log.source_line)
        self.assertEqual('starting jubaclassifier 0.4.3 RPC server at 192.168.122.211:9199', log.message)

    def test_init_jubalog_loglevels(self):
        log = Log('localhost', '2014-05-16 13:58:52,905 28460 WARN  [server_util.cpp:217] starting jubaclassifier 0.4.3 RPC server at 192.168.122.211:9199')
        self.assertEqual(LogLevel.WARN, log.level)

        log = Log('localhost', '2014-05-16 13:58:52,905 28460 ERROR [server_util.cpp:217] starting jubaclassifier 0.4.3 RPC server at 192.168.122.211:9199')
        self.assertEqual(LogLevel.ERROR, log.level)

        log = Log('localhost', '2014-05-16 13:58:52,905 28460 FATAL [server_util.cpp:217] starting jubaclassifier 0.4.3 RPC server at 192.168.122.211:9199')
        self.assertEqual(LogLevel.FATAL, log.level)

    def test_init_jubalog_multiline(self):
        log = Log('localhost', '''2014-05-16 13:58:52,905 28460 FATAL [server_util.cpp:217] hello world\nhello world''')
        self.assertEqual('hello world\nhello world', log.message)

    def test_init_zklog_all(self):
        log = Log('localhost', '2013-05-16 13:58:52,659:28460(0x7f02e99b7740):ZOO_INFO@log_env@712: Client environment:zookeeper.version=zookeeper C client 3.4.5')
        self.assertEqual('zookeeper', log.type)
        self.assertEqual(LogLevel.INFO, log.level)
        self.assertEqual(datetime(2013, 5, 16, 13, 58, 52, 659000), log.time)
        self.assertEqual(28460, log.thread_id)
        self.assertEqual('log_env', log.source)
        self.assertEqual('712', log.source_line)
        self.assertEqual('Client environment:zookeeper.version=zookeeper C client 3.4.5', log.message)

    def test_init_zklog_loglevels(self):
        log = Log('localhost', '2013-05-16 13:58:52,659:28460(0x7f02e99b7740):ZOO_DEBUG@log_env@712: ')
        self.assertEqual(LogLevel.DEBUG, log.level)

        log = Log('localhost', '2013-05-16 13:58:52,659:28460(0x7f02e99b7740):ZOO_INFO@log_env@712: ')
        self.assertEqual(LogLevel.INFO, log.level)

        log = Log('localhost', '2013-05-16 13:58:52,659:28460(0x7f02e99b7740):ZOO_WARN@log_env@712: ')
        self.assertEqual(LogLevel.WARN, log.level)

        log = Log('localhost', '2013-05-16 13:58:52,659:28460(0x7f02e99b7740):ZOO_ERROR@log_env@712: ')
        self.assertEqual(LogLevel.ERROR, log.level)

        log = Log('localhost', '2013-05-16 13:58:52,659:28460(0x7f02e99b7740):ZOO_FATAL@log_env@712: ')
        self.assertEqual(LogLevel.FATAL, log.level)

    def test_init_fail(self):
        self.assertRaises(JubaTestAssertionError, Log, 'localhost', '999999999')

    def test_parse_logs(self):
        entries = Log.parse_logs('localhost', sample_log)
        self.assertEqual(3, len(entries))
        self.assertEqual('zookeeper', entries[0].type)
        self.assertEqual('jubatus', entries[1].type)
        self.assertEqual('jubatus', entries[2].type)

class LogLevelTest(JubaTestCase):
    def test_levels(self):
        self.assertEqual(LogLevel.INFO, LogLevel.normalize('INFO'))
        self.assertEqual(LogLevel.WARN, LogLevel.normalize('WARN'))

    def test_level_fail(self):
        self.assertRaises(ValueError, LogLevel.normalize, 'NONE')

class LogFilterTest(JubaTestCase):
    def setUp(self):
        self.filter = LogFilter(Log.parse_logs('localhost', sample_log))

    def test_type(self):
        self.assertEqual(3, len(self.filter.get()))
        self.assertEqual(0, len(self.filter.type('test').get()))
        self.assertEqual(1, len(self.filter.type('zookeeper').get()))
        self.assertEqual(2, len(self.filter.type('jubatus').get()))

    def test_node(self):
        filter2 = LogFilter(Log.parse_logs('anotherhost', sample_log + sample_log))
        filter3 = LogFilter(self.filter.get() + filter2.get())
        self.assertEqual(9, len(filter3.get()))
        self.assertEqual(3, len(filter3.node('localhost').get()))
        self.assertEqual(6, len(filter3.node('anotherhost').get()))

    def test_level(self):
        self.assertEqual(2, len(self.filter.level(LogLevel.INFO).get()))
        self.assertEqual(1, len(self.filter.level(LogLevel.ERROR).get()))
        self.assertEqual(0, len(self.filter.level(LogLevel.WARN).get()))

    def test_time_range(self):
        log0 = self.filter.get()[0]
        log1 = self.filter.get()[1]
        log2 = self.filter.get()[2]

        begin = log0.time + timedelta(0, 0, 1)
        end = log2.time - timedelta(0, 0, 1)

        result = self.filter.time_range(begin, end)
        self.assertEqual(1, len(result.get()))
        self.assertEqual(log1, result.get()[0])

    def test_message(self):
        self.assertEqual(2, len(self.filter.message('config').get()))
        self.assertEqual(2, len(self.filter.message('2181').get()))

    def test_consume(self):
        log1 = self.filter.get()[1]
        self.assertEqual(1, len(self.filter.consume(log1).get()))

    def test_get(self):
        self.assertEqual(3, len(self.filter.get()))

sample_log = """\
2013-05-16 13:58:52,778:28460(0x7f02e4b03700):ZOO_INFO@check_events@1750: session establishment complete on server [127.0.0.1:2181], sessionId=0x13d8bcf02a2003b, negotiated timeout=10000
2014-08-11 15:07:15,924 5951 INFO  [server_util.cpp:93] load config from zookeeper: localhost:2181
2014-08-11 15:07:15,925 5951 ERROR [server_util.cpp:81] exception when loading config file: Dynamic exception type: jubatus::core::common::exception::runtime_error::what: config does not exist: /jubatus/config/classifier/test
"""
