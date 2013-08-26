Jubatus Distributed Testing Framework
==========================================

Jubatus Distributed Testing Framework (JDTF) provides a framework to write tests against Jubatus clusters.

Requirements
---------------

- Jubatus 0.4.x
- Python 2.7 + Jubatus Python Client
- RHEL 6.x or Ubuntu 12.04 (64-bit)
  - Mac OS X is not supported
- SSH Server/Client

Overview
------------

Basically, JDTF is a extension of unittest module that comes with Python.
JDTF conceals the messy things regarding Jubatus cluster setup; just define the cluster configuration, and write test cases.
The framework automatically runs servers/keepers via SSH on the host you specified and collect logs.

Test results are formatted in xUnit-compatible XML, so that you can easily integrate tests with continuous integration systems of your choice.

Note that this framework does not cover the ZooKeeper cluster control.
ZooKeeper must be installed and started separately.

Have a look at `test/framework/framework.py`; this may be a good start-point to learn about the framework.

Terminology
--------------

- Environment Definition File (envdef.py)
  - Specify the physical configuration of your testing environment, including Jubatus installation path and ZooKeeper nodes.

- Nodes
  - Nodes are logical (both physical or virtual) server where the server/keeper process runs on, identified by IP addresses.

Developing Framework
-----------------------

To run the unittests for the framework, run:

```
PYTHONPATH=lib bin/jubatest --config envdef.py --testcase test/
```

