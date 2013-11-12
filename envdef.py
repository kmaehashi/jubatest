env.prefix('/opt/jubatus')
#env.prefix('/tmp/jubatus')
#env.variable('LD_LIBRARY_PATH', '/tmp/jubatus/lib:/opt/jubatus/lib')
#env.workdir('/tmp/jubatest-work')
env.cluster_prefix('sample-')

env.zookeeper('127.0.0.1', 2181)

env.node('127.0.0.1', range(19199,19299))

env.param('JUBATUS_TUTORIAL_DIR', '/home/kenichi/Development/jubatus-tutorial-python')
env.param('JUBATUS_BENCH_CLASSIFIER', '/home/kenichi/Development/jubatus-benchmark/jubatus-bench-classifier')
env.param('JUBATUS_BENCH_CLASSIFIER_DATASET', '/home/kenichi/Development/jubatus-benchmark/url_svmlight/Day0.svm')
