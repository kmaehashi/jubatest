# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

ANOMALY = 'anomaly'
BANDIT = 'bandit'
BURST = 'burst'
CLASSIFIER = 'classifier'
CLUSTERING = 'clustering'
GRAPH = 'graph'
NEAREST_NEIGHBOR = 'nearest_neighbor'
RECOMMENDER = 'recommender'
REGRESSION = 'regression'
STAT = 'stat'

ALL_ENGINES = [ANOMALY, BANDIT, BURST, CLASSIFIER, CLUSTERING, GRAPH, NEAREST_NEIGHBOR, RECOMMENDER, REGRESSION, STAT]

CONFIGS = {
  CLUSTERING: {
    'gmm':
      {'parameter': {'forgetting_threshold': 0.5, 'compressed_bucket_size': 100, 'bicriteria_base_size': 10, 'bucket_size': 1000, 'seed': 0, 'bucket_length': 2, 'compressor_method': 'compressive_gmm', 'k': 3, 'forgetting_factor': 0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'gmm'}
    ,
    'kmeans':
      {'parameter': {'forgetting_threshold': 0.5, 'compressed_bucket_size': 100, 'bicriteria_base_size': 10, 'bucket_size': 1000, 'seed': 0, 'bucket_length': 2, 'compressor_method': 'compressive_kmeans', 'k': 3, 'forgetting_factor': 0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'kmeans'}
    ,
    'kmeans_combinational_feature':
      {'parameter': {'forgetting_threshold': 0.5, 'compressed_bucket_size': 100, 'bicriteria_base_size': 10, 'bucket_size': 1000, 'seed': 0, 'bucket_length': 2, 'compressor_method': 'compressive_kmeans', 'k': 3, 'forgetting_factor': 0}, 'converter': {'combination_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'kmeans'}
    ,
  },
  STAT: {
    'stat':
      {'window_size': 128}
    ,
  },
  RECOMMENDER: {
    'euclid_lsh':
      {'parameter': {'retain_projection': False, 'hash_num': 64, 'table_num': 4, 'bin_width': 100, 'probe_num': 64, 'seed': 1091}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'euclid_lsh'}
    ,
    'inverted_index':
      {'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'inverted_index'}
    ,
    'inverted_index_unlearn_lru':
      {'parameter': {'unlearner': 'lru', 'unlearner_parameter': {'max_size': 2048}}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'inverted_index'}
    ,
    'lsh':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'lsh'}
    ,
    'lsh_combinational_feature':
      {'parameter': {'hash_num': 64}, 'converter': {'combination_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'lsh'}
    ,
    'minhash':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'minhash'}
    ,
    'nearest_neighbor_recommender_euclid_lsh':
      {'parameter': {'parameter': {'hash_num': 512}, 'method': 'euclid_lsh'}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'nearest_neighbor_recommender'}
    ,
    'nearest_neighbor_recommender_euclid_lsh_unlearn_lru':
      {'parameter': {'unlearner_parameter': {'max_size': 2048}, 'parameter': {'hash_num': 512}, 'method': 'euclid_lsh', 'unlearner': 'lru'}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'nearest_neighbor_recommender'}
    ,
  },
  BURST: {
    'burst':
      {'parameter': {'costcut_threshold': -1, 'window_batch_size': 5, 'max_reuse_batch_num': 5, 'result_window_rotate_size': 5, 'batch_interval': 10}, 'method': 'burst'}
    ,
  },
  GRAPH: {
    'graph_wo_index':
      {'parameter': {'damping_factor': 0.9, 'landmark_num': 5}, 'method': 'graph_wo_index'}
    ,
  },
  REGRESSION: {
    'pa':
      {'parameter': {'sensitivity': 0.1, 'regularization_weight': 3.402823e+38}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'PA'}
    ,
    'pa_combinational_feature':
      {'parameter': {'sensitivity': 0.1, 'regularization_weight': 3.402823e+38}, 'converter': {'combination_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'PA'}
    ,
  },
  BANDIT: {
    'epsilon_greedy':
      {'parameter': {'epsilon': 0.1, 'assume_unrewarded': False}, 'method': 'epsilon_greedy'}
    ,
    'exp3':
      {'parameter': {'assume_unrewarded': False, 'gamma': 0.1}, 'method': 'exp3'}
    ,
    'softmax':
      {'parameter': {'tau': 0.05, 'assume_unrewarded': False}, 'method': 'softmax'}
    ,
    'ucb1':
      {'parameter': {'assume_unrewarded': False}, 'method': 'ucb1'}
    ,
  },
  NEAREST_NEIGHBOR: {
    'euclid_lsh':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'euclid_lsh'}
    ,
    'lsh':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'lsh'}
    ,
    'lsh_combinational_feature':
      {'parameter': {'hash_num': 64}, 'converter': {'combination_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'lsh'}
    ,
    'minhash':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'minhash'}
    ,
  },
  ANOMALY: {
    'light_lof':
      {'parameter': {'nearest_neighbor_num': 10, 'reverse_nearest_neighbor_num': 30, 'parameter': {'hash_num': 64}, 'method': 'euclid_lsh'}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'light_lof'}
    ,
    'light_lof_combinational_feature':
      {'parameter': {'nearest_neighbor_num': 10, 'reverse_nearest_neighbor_num': 30, 'parameter': {'hash_num': 64}, 'method': 'euclid_lsh'}, 'converter': {'combination_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'light_lof'}
    ,
    'light_lof_unlearn_lru':
      {'parameter': {'nearest_neighbor_num': 10, 'reverse_nearest_neighbor_num': 30, 'unlearner': 'lru', 'parameter': {'hash_num': 64}, 'method': 'euclid_lsh', 'unlearner_parameter': {'max_size': 4096}}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'light_lof'}
    ,
    'lof':
      {'parameter': {'nearest_neighbor_num': 10, 'reverse_nearest_neighbor_num': 30, 'parameter': {'retain_projection': False, 'hash_num': 64, 'table_num': 4, 'bin_width': 100, 'probe_num': 64, 'seed': 1091}, 'method': 'euclid_lsh'}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'lof'}
    ,
  },
  CLASSIFIER: {
    'arow':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'AROW'}
    ,
    'arow_combinational_feature':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'combination_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'AROW'}
    ,
    'cw':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'CW'}
    ,
    'nherd':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'NHERD'}
    ,
    'nn':
      {'parameter': {'local_sensitivity': 1, 'nearest_neighbor_num': 128, 'parameter': {'hash_num': 64}, 'method': 'euclid_lsh'}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'NN'}
    ,
    'pa':
      {'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'PA'}
    ,
    'pa1':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'PA1'}
    ,
    'pa2':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'PA2'}
    ,
    'perceptron':
      {'converter': {'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'string_types': {}, 'num_filter_rules': [], 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'type': 'str', 'global_weight': 'bin', 'key': '*'}], 'num_types': {}, 'string_filter_rules': []}, 'method': 'perceptron'}
    ,
  },
}
