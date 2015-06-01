# -*- coding: utf-8 -*-

CLUSTERING = 'clustering'
ANOMALY = 'anomaly'
RECOMMENDER = 'recommender'
NEAREST_NEIGHBOR = 'nearest_neighbor'
BANDIT = 'bandit'
BURST = 'burst'
REGRESSION = 'regression'
STAT = 'stat'
GRAPH = 'graph'
CLASSIFIER = 'classifier'

ALL_ENGINES = ['CLUSTERING', 'ANOMALY', 'RECOMMENDER', 'NEAREST_NEIGHBOR', 'BANDIT', 'BURST', 'REGRESSION', 'STAT', 'GRAPH', 'CLASSIFIER']

CONFIGS = {
  CLUSTERING: {
    'kmeans':
      {u'parameter': {u'forgetting_threshold': 0.5, u'compressed_bucket_size': 100, u'bicriteria_base_size': 10, u'bucket_size': 1000, u'bucket_length': 2, u'compressor_method': u'compressive_kmeans', u'k': 3, u'forgetting_factor': 0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'kmeans'}
    ,
    'gmm':
      {u'parameter': {u'forgetting_threshold': 0.5, u'compressed_bucket_size': 100, u'bicriteria_base_size': 10, u'bucket_size': 1000, u'bucket_length': 2, u'compressor_method': u'compressive_gmm', u'k': 3, u'forgetting_factor': 0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'gmm'}
    ,
    'kmeans_combinational_feature':
      {u'parameter': {u'forgetting_threshold': 0.5, u'compressed_bucket_size': 100, u'bicriteria_base_size': 10, u'bucket_size': 1000, u'bucket_length': 2, u'compressor_method': u'compressive_kmeans', u'k': 3, u'forgetting_factor': 0}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'kmeans'}
    ,
  },
  STAT: {
    'stat':
      {u'window_size': 128}
    ,
  },
  RECOMMENDER: {
    'nearest_neighbor_recommender_euclid_lsh_unlearn_lru':
      {u'parameter': {u'unlearner_parameter': {u'max_size': 2048}, u'parameter': {u'hash_num': 512}, u'method': u'euclid_lsh', u'unlearner': u'lru'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'nearest_neighbor_recommender'}
    ,
    'lsh':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
    'minhash':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'minhash'}
    ,
    'euclid_lsh':
      {u'parameter': {u'retain_projection': False, u'hash_num': 64, u'table_num': 4, u'bin_width': 100, u'probe_num': 64, u'seed': 1091}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'euclid_lsh'}
    ,
    'inverted_index':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'inverted_index'}
    ,
    'nearest_neighbor_recommender_euclid_lsh':
      {u'parameter': {u'parameter': {u'hash_num': 512}, u'method': u'euclid_lsh'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'nearest_neighbor_recommender'}
    ,
    'lsh_combinational_feature':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
  },
  BURST: {
    'burst':
      {u'parameter': {u'costcut_threshold': -1, u'window_batch_size': 5, u'max_reuse_batch_num': 5, u'result_window_rotate_size': 5, u'batch_interval': 10}, u'method': u'burst'}
    ,
  },
  GRAPH: {
    'graph_wo_index':
      {u'parameter': {u'damping_factor': 0.9, u'landmark_num': 5}, u'method': u'graph_wo_index'}
    ,
  },
  CLASSIFIER: {
    'pa':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA'}
    ,
    'nn':
      {u'parameter': {u'local_sensitivity': 1, u'nearest_neighbor_num': 128, u'parameter': {u'hash_num': 64}, u'method': u'euclid_lsh'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'NN'}
    ,
    'arow':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'AROW'}
    ,
    'perceptron':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'perceptron'}
    ,
    'cw':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'CW'}
    ,
    'pa2':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA2'}
    ,
    'pa1':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA1'}
    ,
    'arow_combinational_feature':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'AROW'}
    ,
    'nherd':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'NHERD'}
    ,
  },
  BANDIT: {
    'exp3':
      {u'parameter': {u'assume_unrewarded': False, u'gamma': 0.1}, u'method': u'exp3'}
    ,
    'ucb1':
      {u'parameter': {u'assume_unrewarded': False}, u'method': u'ucb1'}
    ,
    'epsilon_greedy':
      {u'parameter': {u'epsilon': 0.1, u'assume_unrewarded': False}, u'method': u'epsilon_greedy'}
    ,
    'softmax':
      {u'parameter': {u'tau': 0.05, u'assume_unrewarded': False}, u'method': u'softmax'}
    ,
  },
  NEAREST_NEIGHBOR: {
    'lsh':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
    'minhash':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'minhash'}
    ,
    'euclid_lsh':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'euclid_lsh'}
    ,
    'lsh_combinational_feature':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
  },
  ANOMALY: {
    'light_lof_combinational_feature':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'parameter': {u'hash_num': 64}, u'method': u'euclid_lsh'}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'light_lof'}
    ,
    'lof':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'parameter': {u'retain_projection': False, u'hash_num': 64, u'table_num': 4, u'bin_width': 100, u'probe_num': 64, u'seed': 1091}, u'method': u'euclid_lsh'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lof'}
    ,
    'light_lof_unlearn_lru':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'unlearner': u'lru', u'parameter': {u'hash_num': 64}, u'method': u'euclid_lsh', u'unlearner_parameter': {u'max_size': 4096}}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'light_lof'}
    ,
    'light_lof':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'parameter': {u'hash_num': 64}, u'method': u'euclid_lsh'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'light_lof'}
    ,
  },
  REGRESSION: {
    'pa':
      {u'parameter': {u'sensitivity': 0.1, u'regularization_weight': 3.402823e+38}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA'}
    ,
    'pa_combinational_feature':
      {u'parameter': {u'sensitivity': 0.1, u'regularization_weight': 3.402823e+38}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA'}
    ,
  },
}
