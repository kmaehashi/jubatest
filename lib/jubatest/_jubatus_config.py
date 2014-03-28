# -*- coding: utf-8 -*-

ANOMALY = 'anomaly'
GRAPH = 'graph'
CLASSIFIER = 'classifier'
NEAREST_NEIGHBOR = 'nearest_neighbor'
REGRESSION = 'regression'
STAT = 'stat'
CLUSTERING = 'clustering'
RECOMMENDER = 'recommender'

ALL_ENGINES = ['ANOMALY', 'GRAPH', 'CLASSIFIER', 'NEAREST_NEIGHBOR', 'REGRESSION', 'STAT', 'CLUSTERING', 'RECOMMENDER']

CONFIGS = {
  CLUSTERING: {
    'kmeans':
      {u'parameter': {u'forgetting_threshold': 0.5, u'compressed_bucket_size': 100, u'bicriteria_base_size': 10, u'bucket_size': 1000, u'bucket_length': 2, u'compressor_method': u'compressive_kmeans', u'k': 3, u'forgetting_factor': 0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'kmeans'}
    ,
    'gmm':
      {u'parameter': {u'forgetting_threshold': 0.5, u'compressed_bucket_size': 100, u'bicriteria_base_size': 10, u'bucket_size': 1000, u'bucket_length': 2, u'compressor_method': u'compressive_gmm', u'k': 3, u'forgetting_factor': 0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'gmm'}
    ,
  },
  STAT: {
    'stat':
      {u'window_size': 128}
    ,
  },
  RECOMMENDER: {
    'inverted_index':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'inverted_index'}
    ,
    'minhash':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'minhash'}
    ,
    'euclid_lsh':
      {u'parameter': {u'retain_projection': False, u'hash_num': 64, u'table_num': 4, u'bin_width': 100, u'probe_num': 64, u'seed': 1091}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'euclid_lsh'}
    ,
    'lsh':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
  },
  GRAPH: {
    'graph_wo_index':
      {u'parameter': {u'damping_factor': 0.9, u'landmark_num': 5}, u'method': u'graph_wo_index'}
    ,
  },
  REGRESSION: {
    'pa':
      {u'parameter': {u'sensitivity': 0.1, u'regularization_weight': 3.402823e+38}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA'}
    ,
  },
  NEAREST_NEIGHBOR: {
    'minhash':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'minhash'}
    ,
    'euclid_lsh':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'euclid_lsh'}
    ,
    'lsh':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
  },
  ANOMALY: {
    'lof':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'parameter': {u'retain_projection': False, u'hash_num': 64, u'table_num': 4, u'bin_width': 100, u'probe_num': 64, u'seed': 1091}, u'method': u'euclid_lsh'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lof'}
    ,
  },
  CLASSIFIER: {
    'cw':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'CW'}
    ,
    'arow':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'AROW'}
    ,
    'pa1':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA1'}
    ,
    'pa2':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA2'}
    ,
    'nherd':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'NHERD'}
    ,
    'pa':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA'}
    ,
    'perceptron':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'perceptron'}
    ,
  },
}
