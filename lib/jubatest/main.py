# -*- coding: utf-8 -*-

import sys
import argparse
import logging
import traceback

from .logger import setup_logger, log
from .entity import JubaTestEnvironment
from .reporter import JubaTestTextReporter, JubaTestXunitReporter
from .unit import JubaTestRunner, get_loader, get_suite

class JubaTest(object):
    def main(self, args):
        setup_logger('INFO')

        retval = 0
        log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

        try:
            parser = argparse.ArgumentParser(description='Jubatus Distributed Test')

            parser.add_argument('--library',  type=str,                 help='append module search path')
            parser.add_argument('--config',   type=str, required=True,  help='environment configuration file')
            parser.add_argument('--testcase', type=str, required=True,  help='directory to look for test cases')
            parser.add_argument('--pattern',  type=str, default='*.py', help='patterns of test case files')
            parser.add_argument('--xunit',    type=str, default=None,   help='path to store xUnit test report')
            parser.add_argument('--log',      type=str, default='INFO', choices=log_levels, help='log level')

            params = parser.parse_args(args[1:])

            if params.library:
                sys.path.insert(0, params.library)

            if params.log:
                log.setLevel(params.log)

            # TODO: PAINFUL WORKAROUND!
            # tornado 2.x uses the root logger, causing too many warning logs to be directly
            # printed into STDOUT when connection attempts failed. To workaround the problem,
            # we set the log level of the root logger to ERROR so that WARNING logs are
            # silently ignored. tornado 3.x series solves the problem (but msgpack-rpc is
            # not compatible with it yet.)
            logging.getLogger().setLevel(logging.ERROR)

            log.info('starting test session')

            # create new test environment from config file
            env = JubaTestEnvironment.from_config(params.config)

            if not env:
                log.error('failed to create test environment')
                retval = 2
                return

            # define the custom test loader which uses JubaTestSuite
            loader = get_loader(env)()
            loader.suiteClass = get_suite(env)

            # load tests
            log.debug('looking for test cases')
            tests = loader.discover(params.testcase, params.pattern)

            # run tests
            log.debug('starting test run')
            result = JubaTestRunner().run(tests)

            log.info('completed test session')

            if params.xunit:
                log.info('generating report as xUnit XML')
                reporter = JubaTestXunitReporter()
                output = reporter.create_report(result)
                with open(params.xunit, 'w') as f:
                    f.write(output)
            else:
                log.info('generating report as text')
                # mainly intended for debugging purposes
                reporter = JubaTestTextReporter()
                print(reporter.create_report(result))

        except KeyboardInterrupt:
            retval = 127
            log.warning('interrupted')

        except SystemExit:
            raise

        except BaseException as e:
            retval = 2
            log.error('exception: %s (%s)\n%s', e.__class__.__name__, str(e.args), traceback.format_exc())

        finally:
            log.info('end')
            return retval

class JubaTestUtil(object):
    def main(self, args):
        retval = 0
        try:
            parser = argparse.ArgumentParser(description='Jubatus Distributed Test Utility')

            parser.add_argument('--config',          type=str, required=True,  help='environment configuration file')
            parser.add_argument('--list-nodes',      action='store_true',      help='list nodes')
            parser.add_argument('--list-zookeepers', action='store_true',      help='list zookeepers')
            parser.add_argument('--prefix',          action='store_true',      help='get prefix')

            params = parser.parse_args(args[1:])

            env = JubaTestEnvironment.from_config(params.config)

            if params.list_nodes:
                for node in env.nodes:
                    print(node.host),
                    for port in node.ports:
                        print(str(port)),
            if params.list_zookeepers:
                for zk in env.zookeepers:
                    print(zk[0] + ' ' + str(zk[1]))
            if params.prefix:
                print(env.install_path)

        except BaseException as e:
            print(e.message)
        finally:
            return retval
