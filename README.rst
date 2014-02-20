Jubatus Testing Framework
==========================================

Jubatus Testing Framework (JTF) provides a framework to write tests against Jubatus standalone server or Jubatus clusters.

Requirements
---------------

* Jubatus 0.5.x

* Python 2.7.3 + Jubatus Python Client 0.5.x

* RHEL 6.x or Ubuntu 12.04 (64-bit)

  * Mac OS X is not supported (yet)

* SSH Server/Client

Overview
------------

Basically, JTF is a extension of unittest module that comes with Python.
JTF conceals the messy things regarding Jubatus cluster setup; just define the cluster configuration, and write test cases.
The framework automatically runs servers/keepers via SSH on the host you specified and collect logs.

Test results are formatted in xUnit-compatible XML, so that you can easily integrate tests with continuous integration systems of your choice.

Note that this framework does not cover the ZooKeeper cluster control.
ZooKeeper must be installed and started separately.

Terminology
--------------

Environment Definition File
  The file to specify the physical configuration of your testing environment, including Jubatus installation path and ZooKeeper nodes.
  See ``envdef.py`` for the example.

Nodes
  Nodes are logical (either physical or virtual) server where the server/keeper process runs on, identified by IP addresses.

Test Parameters
  Test parameters are pairs of key-values passed to test cases, defined in Environment Definition File.
  You can localize the environment-specific values such as the path to datasets, then later refer to the value in test cases.

Other Resources
------------------

Refer to the `Wiki <https://github.com/kmaehashi/jubatest/wiki>`_ for more information.

Developing Framework
-----------------------

To run the unittests for the framework, run:

::

  make test

