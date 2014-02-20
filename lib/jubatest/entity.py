# -*- coding: utf-8 -*-

"""
Abstraction interface of test environment and clusters/servers/proxies.
"""

import os
import time
import json
import tempfile
import copy

import msgpackrpc

from .process import LocalSubprocess
from .remote import SyncRemoteProcess, AsyncRemoteProcess
from .log import Log, LogFilter
from .unit import JubaSkipTest, JubaTestFixtureFailedError
from .exceptions import JubaTestAssertionError
from .logger import log

from .constants import * # to be used in DSL


"""
How Server Arguments Constructed:
+------------------------------------------------------------------------------------------------------------+
| jubaserver_distributed   --datadir /tmp --zookeeper localhost:2181   --name cluster-name  --rpc-port 19199 |
| jubaserver_stand_alone   --datadir /tmp                              --configpath foo     --rpc-port 19199 |
| jubaproxy                               --zookeeper localhost:2181                        --rpc-port 19199 |
|                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~ |
| Category:                 Node config (+ user-specific options)       Config selector      RPC config      |
| Set by:                   JubaTestEnvironment                         Each Class           JubaRPCServer   |
+------------------------------------------------------------------------------------------------------------+
"""

class JubaTestEnvironment(object):
    """
    Represents the test environment.
    """

    def __init__(self):
        self._nodes = {}
        self._node_records = []
        self._zookeepers = []
        self._prefix = None
        self._workdir = '/tmp'
        self._variables = {}
        self._params = {}
        self._cluster_prefix = ''
        self._generated_clusters = 0
        self._rpc_servers = []

    class ConfigurationDSL(object):
        """
        Provides an internal-DSL for test environment configuration.
        """

        def __init__(self):
            self.env = JubaTestEnvironment()

        def from_source(env, script):
            try:
                exec(compile(script, 'env', 'exec'))
            except SyntaxError as e:
                env.env = None
                log.error('syntax error in environment configuration %s on line %d, at char %d: %s', config, e.lineno, e.offset, e.text)
            except IOError as e:
                env.env = None
                log.error('error when loading environment configuration %s: %s (%s)', config, e.__class__.__name__, str(e.args))
            return env.env

        def node(self, host, ports):
            if type(ports) != list:
                ports = [ports]
            self.env._node_records += [(host,ports)]

        def zookeeper(self, host, port):
            self.env._zookeepers += [(host, port)]

        def prefix(self, prefix):
            self.env._prefix = prefix

        def workdir(self, workdir):
            self.env._workdir = workdir

        def variable(self, key, value):
            self.env._variables[key] = value

        def param(self, key, value):
            self.env._params[key] = value

        def cluster_prefix(self, prefix):
            self.env._cluster_prefix = prefix

    @staticmethod
    def from_config(config):
        log.debug('loading environment configuration: %s', config)
        with open(config) as f:
            env = JubaTestEnvironment.ConfigurationDSL().from_source(f.read())
        log.debug('loaded environment configuration: %s', config)
        return env

    def get_rpc_servers(self):
        return self._rpc_servers

    def finalize_test_case(self, testCase):
        # check servers still running
        for rpc_server in self._rpc_servers:
            if rpc_server.is_running():
                log.warning('{c} is still running! stopping anyway...'.format(c=rpc_server.__class__.__name__))
                rpc_server.stop()

        # check leaked ports
        for number in self._nodes:
            node = self._nodes[number]
            ports_used = node.ports_used()
            if ports_used != 0:
                log.warning('%d leaked port(s) detected on node %d (%s)', ports_used, number, node.get_host())

        # attach logs for failed tests
        if testCase.attachLogs:
            attach_logs = []
            for rpc_server in self._rpc_servers:
                kind = rpc_server.__class__.__name__
                (host, port) = rpc_server.get_host_port()
                log_raw = rpc_server.log_raw()
                attach_logs.append((kind, host, port, log_raw))
            testCase.logs = attach_logs

    def finalize_test_class(self, testClass):
        log.debug('{count} RPC fixtures used for this test class'.format(count=len(self._rpc_servers)))
        self._rpc_servers = []

    #########################################################################
    # Test Fixture Definition                                               #
    #########################################################################

    def cluster(self, service, config, cluster_name=None):
        """
        Constructs new cluster.
        """
        if not cluster_name:
            cluster_name = self._generate_cluster_name()
            log.debug('generated cluster name = %s', cluster_name)
        return JubaCluster(service, config, cluster_name, self._zkargs())

    def server(self, node, cluster, options=[]):
        """
        Constructs new server.
        """
        options2 = options + [
            ('--datadir', node.get_workdir()),
            ('--zookeeper', self._zkargs()),
        ]
        server = JubaServer(node, cluster.service, cluster.name, options2)
        cluster.servers += [server]
        self._rpc_servers.append(server)
        return server

    def server_standalone(self, node, service, config, options=[]):
        """
        Constructs new standalone server.
        """
        options2 = options + [
            ('--datadir', node.get_workdir()),
        ]
        server = JubaStandaloneServer(node, service, config, options2)
        self._rpc_servers.append(server)
        return server

    def proxy(self, node, service, options=[]):
        """
        Constructs new proxy.
        """
        options2 = options + [
            ('--zookeeper', self._zkargs()),
        ]
        proxy = JubaProxy(node, service, options2)
        self._rpc_servers.append(proxy)
        return proxy

    def keeper(self, *args, **kwargs):
        """
        Deprecated.
        """
        return self.proxy(*args, **kwargs)

    def get_node(self, number):
        """
        Returns the given node.
        """
        if number in self._nodes:
            return self._nodes[number]
        if number < len(self._node_records):
            node_info = self._node_records[number]
            node = JubaNode(node_info[0], node_info[1], self._prefix, self._workdir, self._variables)
            self._nodes[number] = node
            return node
        raise JubaSkipTest('insufficient number of nodes')

    def get_param(self, key):
        if key in self._params:
            return self._params[key]
        return None

    #########################################################################
    # Private                                                               #
    #########################################################################

    def _zkargs(self):
        """
        Converts the zookeeper list as string so that it can be given for the argument.
        """
        return ','.join(map(lambda p: p[0] + ':' + str(p[1]), self._zookeepers))

    def _generate_cluster_name(self):
        self._generated_clusters += 1
        return 'jubatest-cluster-%s-%d' % (self._cluster_prefix, self._generated_clusters)

class JubaCluster(object):
    """
    Represents a Jubatus cluster.
    """

    def __init__(self, service, config, name, zk):
        self.service = service
        self.config = config
        self.name = name
        self.zk = zk
        self.servers = []
        self.configure()

    def start(self):
        # start all servers
        for server in self.servers:
            server.start()

    def stop(self):
        # stop all servers
        for server in self.servers:
            server.stop()

    def configure(self):
        if not self._is_command_available('jubaconfig'):
            raise JubaSkipTest('jubaconfig command is not available')
        log.debug('configuring cluster with jubaconfig')
        args = ['jubaconfig', '--cmd', 'write', '--file', '/dev/stdin', '--type', self.service, '--name', self.name, '--zookeeper', self.zk]
        proc = LocalSubprocess(args)
        proc.start()
        if proc.wait(json.dumps(self.config)) != 0:
            raise JubaTestFixtureFailedError('jubaconfig failed: %s\n%s' % (proc.stdout, proc.stderr))

    def _is_command_available(self, command):
        """
        Test if the given command is in PATH.
        """
        for p in os.environ['PATH'].split(os.pathsep):
            if os.path.exists(os.path.join(p, command)):
                return True
        return False

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

class JubaNode(object):
    """
    Represents a (physical) test node.
    """

    def __init__(self, host, ports, prefix, workdir, variables):
        self._host = host
        self._ports = ports
        self._prefix = prefix
        self._workdir = workdir
        self._variables = variables
        self._free_ports = copy.copy(ports)

    def get_host(self):
        return self._host

    def get_workdir(self):
        return self._workdir

    def lease_port(self):
        """
        Leases a port from the port pool.
        """
        if len(self._free_ports) == 0:
            raise JubaSkipTest('insufficient number of ports for node %s' % self._host)
        port = self._free_ports.pop(0)
        log.debug('leased port %d for host %s', port, self._host)
        return port

    def free_port(self, port):
        """
        Returns the given port to the poot pool.
        """
        if port in self._ports:
            if port not in self._free_ports:
                self._free_ports += [port]
                log.debug('freed port %d for host %s', port, self._host)
            else:
                raise JubaTestAssertionError('double free for port %d on host %s detected' % (port, self._host))
        else:
            raise JubaTestAssertionError('port %d is not a member port of host %s' % (port, self._host))

    def ports_used(self):
        """
        Returns number of ports in use.
        """
        return len(self._ports) - len(self._free_ports)

    def put_file(self, data, to_path=None):
        """
        Put the contents to the given path
        """
        if not to_path:
            log.debug('creating temporary file on host %s', self._host)
            to_path = SyncRemoteProcess.run(self._host, ['mktemp', '--tmpdir=' + self._workdir, 'jubatest.tmp.XXXXXXXXXX']).rstrip()
            log.debug('created temporary file on host %s: %s', self._host, to_path)
        with tempfile.NamedTemporaryFile() as tmp_file:
            tmp_file.write(str(data))
            tmp_file.flush()
            log.debug('sending file %s to host %s: %s', tmp_file.name, self._host, to_path)
            SyncRemoteProcess.put_file(self._host, tmp_file.name, to_path)
            log.debug('sent file %s to host %s: %s', tmp_file.name, self._host, to_path)
        return to_path

    def delete_file(self, path):
        """
        Delete the file
        """
        log.debug('deleting file %s on host %s', path, self._host)
        SyncRemoteProcess.run(self._host, ['rm', '-f', path])
        log.debug('deleted file %s on host %s', path, self._host)

    def get_file(self, from_path, to_path=None):
        """
        Returns the contents of the given file.
        """
        tmp_file = None
        if not to_path:
            tmp_file = tempfile.NamedTemporaryFile()
            to_path = tmp_file.name
        try:
            log.debug('downloading file %s on host %s to %s', from_path, self._host, to_path)
            SyncRemoteProcess.get_file(self._host, from_path, to_path)
            log.debug('downloaded file %s on host %s to %s', from_path, self._host, to_path)
            if tmp_file:
                data = tmp_file.read()
            else:
                with open(to_path, 'r') as f:
                    data = f.read()
            return data
        finally:
            if tmp_file:
                tmp_file.close()

    def run_process(self, args):
        return SyncRemoteProcess.run(self._host, args, self._envvars())

    def get_process(self, args):
        return AsyncRemoteProcess(self._host, args, self._envvars())

    def _envvars(self):
        envvars2 = {}
        if self._prefix:
            envvars2['PATH'] = self._prefix + '/bin' + ':' + '${PATH}'
            envvars2['LD_LIBRARY_PATH'] = self._prefix + '/lib' + ':' + self._prefix + '/lib64'
        envvars2.update(self._variables)
        return envvars2

class JubaRPCServer(object):
    """
    Defines the common functions among Jubatus servers and proxies.
    """

    CLIENT_TIMEOUT = 5 # TODO make it configurable

    def __init__(self, node, service, options):
        self.node = node
        self.service = service
        self.options = options
        self.port = -1
        self.backend = None
        self._log_filter = None

    def start(self, sync=True):
        """
        Starts the RPC server.
        """
        if self.is_running():
            raise JubaTestFixtureFailedError('this instance is already running')

        self.port = self.node.lease_port()
        options2 = self.options + [
            ('--rpc-port', self.port),
        ]
        flat_opts = self._flatten_options(options2)
        self.backend = self.node.get_process([self.program()] + flat_opts)

        log.debug('starting remote process')
        self.backend.start()
        if not sync:
            return

        log.debug('waiting for RPC server to startup')
        delay = 20000 # usec
        for i in range(8):
            time.sleep(delay / 1000000.0) # usec -> sec
            if self.is_ready():
                log.debug('RPC server ready after %d retries', i)
                return
            delay *= 2
        try:
            log.warning('RPC server startup sync timed out, stopping')
            self.stop()
        finally:
            raise JubaTestFixtureFailedError('failed to start server: stdout = %s, stderr = %s' % (self.backend.stdout, self.backend.stderr))

    def stop(self):
        """
        Stops the RPC server.
        """
        if not self.is_running():
            raise JubaTestFixtureFailedError('this instance is not running')

        log.debug('stopping remote process')
        self.backend.stop()
        self.node.free_port(self.port)

    def is_running(self):
        """
        Tests if the backed process is still running.
        """
        return self.backend and self.backend.is_running()

    def get_client(self, cluster_name=None):
        """
        Returns the client instance for this RPC server.
        """
        if not cluster_name:
            cluster_name = self.cluster_name()
        cli = None
        try:
            cli_class = self._get_class('.'.join(['jubatus', self.service, 'client', self.service.capitalize()]))
            cli = cli_class(self.node.get_host(), self.port, cluster_name, self.CLIENT_TIMEOUT)
        except BaseException as e:
            raise JubaTestFixtureFailedError('failed to create client class for %s (%s)' % (self.service, e.message))
        return cli

    def get_client_type(self, typename):
        """
        Returns the client data structure.
        """
        c = None
        try:
            if typename == 'datum':
                # migration support for Jubatus 0.4.5
                datumClass = self._get_class('.'.join(['jubatus', 'common', 'Datum']))
                class Datum04(datumClass):
                    def __init__(self_inner, string_values, num_values):
                        datumClass.__init__(self_inner)
                        self_inner.string_values = string_values
                        self_inner.num_values = num_values
                c = Datum04
            elif typename == 'Datum':
                c = self._get_class('.'.join(['jubatus', 'common', 'Datum']))
            else:
                c = self._get_class('.'.join(['jubatus', self.service, 'types', typename]))
        except BaseException as e:
            raise JubaTestFixtureFailedError('failed to create client type %s (%s)' % (typename, e.message))
        return c

    @property
    def types(self):
        class TypeAccessor():
            def __getattr__(self_inner, name):
                    return self.get_client_type(name)
        return TypeAccessor()

    def get_host_port(self):
        """
        Returns the host/port for this RPC server as tuple.
        """
        return (self.node.get_host(), self.port)

    def log(self):
        """
        Returns Jubatus LogFilter for this RPC server.
        """
        return self._get_log_filter().type('jubatus')

    def log_zk(self):
        """
        Returns ZooKeeper LogFilter for this RPC server.
        """
        return self._get_log_filter().type('zookeeper')

    def log_all(self):
        """
        Returns LogFilter for this RPC server.
        """
        return self._get_log_filter()

    def log_raw(self):
        """
        Returns raw log.
        """
        if self.backend and self.backend.stderr is not None:
            return self.backend.stderr
        raise JubaTestAssertionError('no log data collected (maybe the server is not stopped yet?)')

    def _get_log_filter(self):
        if self.backend and self.backend.stderr:
            if not self._log_filter:
                self._log_filter = LogFilter(Log.parse_logs(self.node, self.backend.stderr))
            return self._log_filter
        log.warning('log data is not available (maybe the server is not stopped yet?)')
        raise JubaTestAssertionError('no log data collected (maybe the server is not stopped yet?)')

    def is_ready(self):
        """
        Pings the RPC server in one-shot.
        """
        cli = msgpackrpc.Client(msgpackrpc.Address(self.node.get_host(), self.port))
        cli._timeout = 1
        try:
            cli.call('__dummy_method__')
            return True
        except msgpackrpc.error.RPCError as e:
            if e.args[0] == 1: # "no such method"
                return True    # ... means server is fully up
        finally:
            cli.close()
        return False

    def cluster_name(self):
        """
        Name of the cluster; override in subclasses.
        """
        raise NotImplementedError

    def program(self):
        """
        Name of program; override in subclasses.
        """
        raise NotImplementedError

    def _get_class(self, name):
        """
        Imports and returns the class of given name.
        """
        levels = name.split('.')
        (package, module, basename) = (levels[0], '.'.join(levels[:-1]), levels[-1])
        return getattr(__import__(module, fromlist=[package]), basename)

    def _flatten_options(self, options):
        """
        Flattens the options (list of tuples) to list so that it can be used as an argument.
        """
        args = []
        seen = set()
        for opt in options:
            opt_key = str(opt[0])
            opt_val = str(opt[1])
            if opt_key in seen:
                log.debug('squashed duplicated option: %s = %s', opt_key, opt_val)
                continue
            seen.add(opt_key)
            args += [opt_key, opt_val]
        return args

    def __enter__(self):
        self.start()
        return self.get_client()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

    def __str__(self):
        try:
            return str(self.log_all())
        except:
            return super(JubaRPCServer, self).__str__()

class JubaServer(JubaRPCServer):
    """
    Represents a Jubatus server.
    """

    def __init__(self, node, service, name, options):
        self.server_id = None
        options2 = options
        if name:
            self.name = name
            options2 += [
                ('--name', name),
            ]
        else:
            self.name = ''
        super(JubaServer, self).__init__(node, service, options2)

    def cluster_name(self):
        return self.name

    def program(self):
        return 'juba' + self.service

    def get_id(self):
        """
        ID is a server identifier in form of "${IP}_${PORT}".
        """
        if self.server_id:
            log.debug('reusing cached server ID = %s', self.server_id)
            return self.server_id

        log.debug('sending request: server ID')
        cli = msgpackrpc.Client(msgpackrpc.Address(self.node.get_host(), self.port))
        server_id = cli.call('get_status', '').popitem()[0]
        cli.close()
        log.debug('got reply: server ID = %s', server_id)
        self.server_id = server_id
        return server_id

    def get_saved_model(self, model_id):
        log.debug('sending request: saved model ID %s', model_id)
        model_file = self.node.get_file(self.node.get_workdir() + '/' + self.get_id() + '_jubatus_' + model_id + '.jubatus')
        log.debug('got reply: saved model ID %s', model_id)
        return model_file

class JubaStandaloneServer(JubaServer):
    """
    Represents a Jubatus servers that run in standalone mode.
    """
    def __init__(self, node, service, config, options):
        log.debug('transfering temporary configuration file for a standalone server')
        self._config = config
        self._config_path = node.put_file(json.dumps(config))
        log.debug('transferred temporary configuration file for a standalone server: %s', self._config_path)
        options2 = options + [
            ('--configpath', self._config_path),
        ]
        super(JubaStandaloneServer, self).__init__(node, service, None, options2)

class JubaProxy(JubaRPCServer):
    """
    Represents a Jubatus proxy.
    """

    def wait_for_servers(self, *servers):
        # poll for every 1 second, timeout in 5 seconds
        log.debug('waiting for servers to be registered: %d' % len(servers))
        (server_id, cluster_name) = ('', '')
        for delay in [0] + [1] * 5:
            time.sleep(delay)
            for server in servers:
                server_id = server.get_id()
                cluster_name = server.name
                if not server_id in self.get_cluster_members(server):
                    log.debug('member %s in cluster %s not registered yet', server_id, cluster_name)
                    break
            else:
                log.debug('all servers ready')
                return
        raise JubaTestFixtureFailedError('wait timed-out for member %s in cluster %s' % (server_id, cluster_name))

    def get_cluster_members(self, cluster):
        log.debug('requesting Jubatus cluster members for cluster %s', cluster.name)
        cli = msgpackrpc.Client(msgpackrpc.Address(self.node.get_host(), self.port))
        try:
            members = cli.call('get_status', cluster.name).keys()
        except msgpackrpc.error.RPCError as e:
            if e.args[0] != 'no server found: ' + cluster.name:
                raise
            members = []
        cli.close()
        log.debug('got Jubatus cluster members for cluster %s: %d', cluster.name, len(members))
        return members

    def cluster_name(self):
        raise JubaTestAssertionError('Cannot assume cluster name for proxies!')

    def program(self):
        return 'juba' + self.service + '_proxy'

    def __enter__(self):
        raise JubaTestAssertionError('Cannot use `with` syntax with proxies!')

class JubaKeeper(JubaProxy):
    """
    DEPRECATED
    """
    pass
