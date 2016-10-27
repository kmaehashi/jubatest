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
WEIGHT = 'weight'

ALL_ENGINES = [ANOMALY, BANDIT, BURST, CLASSIFIER, CLUSTERING, GRAPH, NEAREST_NEIGHBOR, RECOMMENDER, REGRESSION, STAT, WEIGHT]

CONFIGS = {
  CLUSTERING: {
    'dbscan':
      {u'compressor_method': u'simple', u'compressor_parameter': {u'bucket_size': 100}, u'parameter': {u'min_core_point': 3, u'eps': 2.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'dbscan'}
    ,
    'default':
      {u'compressor_method': u'simple', u'compressor_parameter': {u'bucket_size': 1000}, u'parameter': {u'k': 3, u'seed': 0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {u'bigram': {u'method': u'ngram', u'char_num': u'2'}, u'unigram': {u'method': u'ngram', u'char_num': u'1'}, u'trigram': {u'method': u'ngram', u'char_num': u'3'}}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'tf', u'type': u'bigram', u'global_weight': u'idf', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'kmeans'}
    ,
    'gmm':
      {u'compressor_method': u'compressive', u'compressor_parameter': {u'forgetting_threshold': 0.5, u'compressed_bucket_size': 100, u'bicriteria_base_size': 10, u'seed': 0, u'bucket_length': 2, u'bucket_size': 1000, u'forgetting_factor': 0}, u'parameter': {u'k': 3, u'seed': 0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'gmm'}
    ,
    'kmeans':
      {u'compressor_method': u'simple', u'compressor_parameter': {u'bucket_size': 100}, u'parameter': {u'k': 3, u'seed': 0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'kmeans'}
    ,
    'kmeans_combinational_feature':
      {u'compressor_method': u'compressive', u'compressor_parameter': {u'forgetting_threshold': 0.5, u'compressed_bucket_size': 100, u'bicriteria_base_size': 10, u'seed': 0, u'bucket_length': 2, u'bucket_size': 1000, u'forgetting_factor': 0}, u'parameter': {u'k': 3, u'seed': 0}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'kmeans'}
    ,
  },
  STAT: {
    'default':
      {u'window_size': 128}
    ,
    'stat':
      {u'window_size': 128}
    ,
  },
  RECOMMENDER: {
    'default':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {u'bigram': {u'method': u'ngram', u'char_num': u'2'}, u'unigram': {u'method': u'ngram', u'char_num': u'1'}, u'trigram': {u'method': u'ngram', u'char_num': u'3'}}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'tf', u'type': u'bigram', u'global_weight': u'idf', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'inverted_index'}
    ,
    'euclid_lsh':
      {u'parameter': {u'hash_num': 64, u'bin_width': 100, u'seed': 1091, u'table_num': 4, u'probe_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'euclid_lsh'}
    ,
    'euclid_lsh_unlearn_lru':
      {u'parameter': {u'hash_num': 64, u'table_num': 4, u'bin_width': 100, u'unlearner': u'lru', u'probe_num': 64, u'seed': 1091, u'unlearner_parameter': {u'max_size': 2048}}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'euclid_lsh'}
    ,
    'inverted_index':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'inverted_index'}
    ,
    'inverted_index_euclid':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'inverted_index_euclid'}
    ,
    'inverted_index_euclid_unlearn_lru':
      {u'parameter': {u'unlearner': u'lru', u'unlearner_parameter': {u'max_size': 2048}}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'inverted_index_euclid'}
    ,
    'inverted_index_unlearn_lru':
      {u'parameter': {u'unlearner': u'lru', u'unlearner_parameter': {u'max_size': 2048}}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'inverted_index'}
    ,
    'lsh':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
    'lsh_combinational_feature':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
    'lsh_unlearn_lru':
      {u'parameter': {u'hash_num': 64, u'unlearner': u'lru', u'unlearner_parameter': {u'max_size': 2048}}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
    'minhash':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'minhash'}
    ,
    'minhash_unlearn_lru':
      {u'parameter': {u'hash_num': 64, u'unlearner': u'lru', u'unlearner_parameter': {u'max_size': 2048}}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'minhash'}
    ,
    'nearest_neighbor_recommender_euclid_lsh':
      {u'parameter': {u'parameter': {u'hash_num': 512}, u'method': u'euclid_lsh'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'nearest_neighbor_recommender'}
    ,
    'nearest_neighbor_recommender_euclid_lsh_unlearn_lru':
      {u'parameter': {u'unlearner_parameter': {u'max_size': 2048}, u'parameter': {u'hash_num': 512}, u'method': u'euclid_lsh', u'unlearner': u'lru'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'nearest_neighbor_recommender'}
    ,
  },
  WEIGHT: {
    'default':
      {u'converter': {u'binary_types': {}, u'num_filter_types': {u'sigmoid': {u'bias': u'5', u'method': u'sigmoid_normalization', u'gain': u'0.05'}, u'linear': {u'max': u'100', u'method': u'linear_normalization', u'min': u'0'}, u'gaussian': {u'standard_deviation': u'2.3', u'average': u'80', u'method': u'gaussian_normalization'}}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {u'bigram': {u'method': u'ngram', u'char_num': u'2'}, u'unigram': {u'method': u'ngram', u'char_num': u'1'}, u'trigram': {u'method': u'ngram', u'char_num': u'3'}}, u'num_filter_rules': [], u'string_filter_types': {}, u'binary_rules': [], u'string_rules': [{u'sample_weight': u'tf', u'type': u'unigram', u'global_weight': u'idf', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}}
    ,
  },
  BURST: {
    'burst':
      {u'parameter': {u'costcut_threshold': -1, u'window_batch_size': 5, u'max_reuse_batch_num': 5, u'result_window_rotate_size': 5, u'batch_interval': 10}, u'method': u'burst'}
    ,
    'default':
      {u'parameter': {u'costcut_threshold': -1, u'window_batch_size': 5, u'max_reuse_batch_num': 5, u'result_window_rotate_size': 5, u'batch_interval': 10}, u'method': u'burst'}
    ,
  },
  GRAPH: {
    'default':
      {u'parameter': {u'damping_factor': 0.9, u'landmark_num': 5}, u'method': u'graph_wo_index'}
    ,
    'graph_wo_index':
      {u'parameter': {u'damping_factor': 0.9, u'landmark_num': 5}, u'method': u'graph_wo_index'}
    ,
  },
  REGRESSION: {
    'default':
      {u'parameter': {u'sensitivity': 0.1, u'regularization_weight': 3.402823e+38}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {u'bigram': {u'method': u'ngram', u'char_num': u'2'}, u'unigram': {u'method': u'ngram', u'char_num': u'1'}, u'trigram': {u'method': u'ngram', u'char_num': u'3'}}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'tf', u'type': u'bigram', u'global_weight': u'idf', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA1'}
    ,
    'pa':
      {u'parameter': {u'sensitivity': 0.1, u'regularization_weight': 3.402823e+38}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA1'}
    ,
    'pa_combinational_feature':
      {u'parameter': {u'sensitivity': 0.1, u'regularization_weight': 3.402823e+38}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA1'}
    ,
  },
  BANDIT: {
    'default':
      {u'parameter': {u'assume_unrewarded': False}, u'method': u'ucb1'}
    ,
    'epsilon_greedy':
      {u'parameter': {u'epsilon': 0.1, u'assume_unrewarded': False}, u'method': u'epsilon_greedy'}
    ,
    'exp3':
      {u'parameter': {u'assume_unrewarded': False, u'gamma': 0.1}, u'method': u'exp3'}
    ,
    'softmax':
      {u'parameter': {u'tau': 0.05, u'assume_unrewarded': False}, u'method': u'softmax'}
    ,
    'ucb1':
      {u'parameter': {u'assume_unrewarded': False}, u'method': u'ucb1'}
    ,
  },
  NEAREST_NEIGHBOR: {
    'default':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {u'bigram': {u'method': u'ngram', u'char_num': u'2'}, u'unigram': {u'method': u'ngram', u'char_num': u'1'}, u'trigram': {u'method': u'ngram', u'char_num': u'3'}}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'tf', u'type': u'bigram', u'global_weight': u'idf', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
    'euclid_lsh':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'euclid_lsh'}
    ,
    'lsh':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
    'lsh_combinational_feature':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
    'lsh_multithread':
      {u'parameter': {u'hash_num': 64, u'threads': 2}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lsh'}
    ,
    'minhash':
      {u'parameter': {u'hash_num': 64}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'minhash'}
    ,
  },
  ANOMALY: {
    'default':
      {u'parameter': {u'parameter': {}, u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'ignore_kth_same_point': True, u'method': u'inverted_index_euclid'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {u'bigram': {u'method': u'ngram', u'char_num': u'2'}, u'unigram': {u'method': u'ngram', u'char_num': u'1'}, u'trigram': {u'method': u'ngram', u'char_num': u'3'}}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'tf', u'type': u'bigram', u'global_weight': u'idf', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lof'}
    ,
    'light_lof':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'parameter': {u'hash_num': 64}, u'method': u'euclid_lsh'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'light_lof'}
    ,
    'light_lof_combinational_feature':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'parameter': {u'hash_num': 64}, u'method': u'euclid_lsh'}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'light_lof'}
    ,
    'light_lof_unlearn_lru':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'unlearner': u'lru', u'parameter': {u'hash_num': 64}, u'method': u'euclid_lsh', u'unlearner_parameter': {u'max_size': 4096}}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'light_lof'}
    ,
    'lof':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'parameter': {u'hash_num': 64, u'bin_width': 100, u'seed': 1091, u'table_num': 4, u'probe_num': 64}, u'method': u'euclid_lsh'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lof'}
    ,
    'lof_inverted_index_euclid':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'parameter': {}, u'method': u'inverted_index_euclid'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lof'}
    ,
    'lof_unlearner_lru':
      {u'parameter': {u'nearest_neighbor_num': 10, u'reverse_nearest_neighbor_num': 30, u'unlearner': u'lru', u'parameter': {u'hash_num': 64, u'bin_width': 100, u'seed': 1091, u'table_num': 4, u'probe_num': 64}, u'method': u'euclid_lsh', u'unlearner_parameter': {u'max_size': 4096}}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'lof'}
    ,
  },
  CLASSIFIER: {
    'arow':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'AROW'}
    ,
    'arow_combinational_feature':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'combination_types': {}, u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'combination_rules': [{u'key_left': u'*', u'type': u'mul', u'key_right': u'*'}], u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'AROW'}
    ,
    'cosine':
      {u'parameter': {u'nearest_neighbor_num': 16, u'local_sensitivity': 0.1}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'cosine'}
    ,
    'cw':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'CW'}
    ,
    'default':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {u'bigram': {u'method': u'ngram', u'char_num': u'2'}, u'unigram': {u'method': u'ngram', u'char_num': u'1'}, u'trigram': {u'method': u'ngram', u'char_num': u'3'}}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'tf', u'type': u'bigram', u'global_weight': u'idf', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'AROW'}
    ,
    'euclidean':
      {u'parameter': {u'nearest_neighbor_num': 16, u'local_sensitivity': 0.1}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'euclidean'}
    ,
    'nherd':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'NHERD'}
    ,
    'nn':
      {u'parameter': {u'local_sensitivity': 1, u'nearest_neighbor_num': 128, u'parameter': {u'hash_num': 64}, u'method': u'euclid_lsh'}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'NN'}
    ,
    'pa':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA'}
    ,
    'pa1':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA1'}
    ,
    'pa2':
      {u'parameter': {u'regularization_weight': 1.0}, u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'PA2'}
    ,
    'perceptron':
      {u'converter': {u'num_filter_types': {}, u'num_rules': [{u'type': u'num', u'key': u'*'}], u'string_types': {}, u'num_filter_rules': [], u'string_filter_types': {}, u'string_rules': [{u'sample_weight': u'bin', u'type': u'str', u'global_weight': u'bin', u'key': u'*'}], u'num_types': {}, u'string_filter_rules': []}, u'method': u'perceptron'}
    ,
  },
}
