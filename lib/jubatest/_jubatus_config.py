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
  STAT: {
    'default':
      {'window_size': 128}
    ,
    'stat':
      {'window_size': 128}
    ,
  },
  WEIGHT: {
    'default':
      {'converter': {'string_types': {'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}, 'unigram': {'method': 'ngram', 'char_num': '1'}}, 'num_filter_types': {'linear': {'method': 'linear_normalization', 'min': '0', 'max': '100'}, 'sigmoid': {'method': 'sigmoid_normalization', 'gain': '0.05', 'bias': '5'}, 'gaussian': {'method': 'gaussian_normalization', 'standard_deviation': '2.3', 'average': '80'}}, 'binary_rules': [], 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'binary_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'tf', 'global_weight': 'idf', 'type': 'unigram', 'key': '*'}]}}
    ,
  },
  NEAREST_NEIGHBOR: {
    'default':
      {'method': 'lsh', 'parameter': {'hash_num': 64}, 'converter': {'string_types': {'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}, 'unigram': {'method': 'ngram', 'char_num': '1'}}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'tf', 'global_weight': 'idf', 'type': 'bigram', 'key': '*'}]}}
    ,
    'euclid_lsh':
      {'method': 'euclid_lsh', 'parameter': {'hash_num': 64}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'lsh':
      {'method': 'lsh', 'parameter': {'hash_num': 64}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'lsh_combinational_feature':
      {'method': 'lsh', 'parameter': {'hash_num': 64}, 'converter': {'string_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}], 'combination_types': {}}}
    ,
    'lsh_multithread':
      {'method': 'lsh', 'parameter': {'threads': 2, 'hash_num': 64}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'minhash':
      {'method': 'minhash', 'parameter': {'hash_num': 64}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
  },
  REGRESSION: {
    'default':
      {'method': 'PA', 'parameter': {'sensitivity': 0.1, 'regularization_weight': 3.402823e+38}, 'converter': {'string_types': {'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}, 'unigram': {'method': 'ngram', 'char_num': '1'}}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'tf', 'global_weight': 'idf', 'type': 'bigram', 'key': '*'}]}}
    ,
    'pa':
      {'method': 'PA', 'parameter': {'sensitivity': 0.1, 'regularization_weight': 3.402823e+38}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'pa_combinational_feature':
      {'method': 'PA', 'parameter': {'sensitivity': 0.1, 'regularization_weight': 3.402823e+38}, 'converter': {'string_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}], 'combination_types': {}}}
    ,
  },
  GRAPH: {
    'default':
      {'method': 'graph_wo_index', 'parameter': {'damping_factor': 0.9, 'landmark_num': 5}}
    ,
    'graph_wo_index':
      {'method': 'graph_wo_index', 'parameter': {'damping_factor': 0.9, 'landmark_num': 5}}
    ,
  },
  BANDIT: {
    'default':
      {'method': 'ucb1', 'parameter': {'assume_unrewarded': False}}
    ,
    'epsilon_greedy':
      {'method': 'epsilon_greedy', 'parameter': {'epsilon': 0.1, 'assume_unrewarded': False}}
    ,
    'exp3':
      {'method': 'exp3', 'parameter': {'gamma': 0.1, 'assume_unrewarded': False}}
    ,
    'softmax':
      {'method': 'softmax', 'parameter': {'tau': 0.05, 'assume_unrewarded': False}}
    ,
    'ucb1':
      {'method': 'ucb1', 'parameter': {'assume_unrewarded': False}}
    ,
  },
  CLUSTERING: {
    'default':
      {'method': 'kmeans', 'parameter': {'seed': 0, 'bicriteria_base_size': 10, 'forgetting_threshold': 0.5, 'bucket_size': 1000, 'k': 3, 'bucket_length': 2, 'compressor_method': 'simple', 'forgetting_factor': 0, 'compressed_bucket_size': 100}, 'converter': {'string_types': {'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}, 'unigram': {'method': 'ngram', 'char_num': '1'}}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'tf', 'global_weight': 'idf', 'type': 'bigram', 'key': '*'}]}}
    ,
    'gmm':
      {'method': 'gmm', 'parameter': {'seed': 0, 'bicriteria_base_size': 10, 'forgetting_threshold': 0.5, 'bucket_size': 1000, 'k': 3, 'bucket_length': 2, 'compressor_method': 'compressive_gmm', 'forgetting_factor': 0, 'compressed_bucket_size': 100}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'kmeans':
      {'method': 'kmeans', 'parameter': {'seed': 0, 'bicriteria_base_size': 10, 'forgetting_threshold': 0.5, 'bucket_size': 1000, 'k': 3, 'bucket_length': 2, 'compressor_method': 'compressive_kmeans', 'forgetting_factor': 0, 'compressed_bucket_size': 100}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'kmeans_combinational_feature':
      {'method': 'kmeans', 'parameter': {'seed': 0, 'bicriteria_base_size': 10, 'forgetting_threshold': 0.5, 'bucket_size': 1000, 'k': 3, 'bucket_length': 2, 'compressor_method': 'compressive_kmeans', 'forgetting_factor': 0, 'compressed_bucket_size': 100}, 'converter': {'string_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}], 'combination_types': {}}}
    ,
  },
  RECOMMENDER: {
    'default':
      {'method': 'inverted_index', 'converter': {'string_types': {'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}, 'unigram': {'method': 'ngram', 'char_num': '1'}}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'tf', 'global_weight': 'idf', 'type': 'bigram', 'key': '*'}]}}
    ,
    'euclid_lsh':
      {'method': 'euclid_lsh', 'parameter': {'probe_num': 64, 'hash_num': 64, 'bin_width': 100, 'table_num': 4, 'seed': 1091}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'euclid_lsh_unlearn_lru':
      {'method': 'euclid_lsh', 'parameter': {'probe_num': 64, 'hash_num': 64, 'unlearner_parameter': {'max_size': 2048}, 'unlearner': 'lru', 'bin_width': 100, 'table_num': 4, 'seed': 1091}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'inverted_index':
      {'method': 'inverted_index', 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'inverted_index_euclid':
      {'method': 'inverted_index_euclid', 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'inverted_index_euclid_unlearn_lru':
      {'method': 'inverted_index_euclid', 'parameter': {'unlearner': 'lru', 'unlearner_parameter': {'max_size': 2048}}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'inverted_index_unlearn_lru':
      {'method': 'inverted_index', 'parameter': {'unlearner': 'lru', 'unlearner_parameter': {'max_size': 2048}}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'lsh':
      {'method': 'lsh', 'parameter': {'hash_num': 64}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'lsh_combinational_feature':
      {'method': 'lsh', 'parameter': {'hash_num': 64}, 'converter': {'string_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}], 'combination_types': {}}}
    ,
    'lsh_unlearn_lru':
      {'method': 'lsh', 'parameter': {'hash_num': 64, 'unlearner_parameter': {'max_size': 2048}, 'unlearner': 'lru'}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'minhash':
      {'method': 'minhash', 'parameter': {'hash_num': 64}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'minhash_unlearn_lru':
      {'method': 'minhash', 'parameter': {'hash_num': 64, 'unlearner_parameter': {'max_size': 2048}, 'unlearner': 'lru'}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'nearest_neighbor_recommender_euclid_lsh':
      {'method': 'nearest_neighbor_recommender', 'parameter': {'method': 'euclid_lsh', 'parameter': {'hash_num': 512}}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'nearest_neighbor_recommender_euclid_lsh_unlearn_lru':
      {'method': 'nearest_neighbor_recommender', 'parameter': {'method': 'euclid_lsh', 'parameter': {'hash_num': 512}, 'unlearner_parameter': {'max_size': 2048}, 'unlearner': 'lru'}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
  },
  BURST: {
    'burst':
      {'method': 'burst', 'parameter': {'result_window_rotate_size': 5, 'max_reuse_batch_num': 5, 'batch_interval': 10, 'window_batch_size': 5, 'costcut_threshold': -1}}
    ,
    'default':
      {'method': 'burst', 'parameter': {'result_window_rotate_size': 5, 'max_reuse_batch_num': 5, 'batch_interval': 10, 'window_batch_size': 5, 'costcut_threshold': -1}}
    ,
  },
  CLASSIFIER: {
    'arow':
      {'method': 'AROW', 'parameter': {'regularization_weight': 1.0}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'arow_combinational_feature':
      {'method': 'AROW', 'parameter': {'regularization_weight': 1.0}, 'converter': {'string_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}], 'combination_types': {}}}
    ,
    'cosine':
      {'method': 'cosine', 'parameter': {'nearest_neighbor_num': 16, 'local_sensitivity': 0.1}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'cw':
      {'method': 'CW', 'parameter': {'regularization_weight': 1.0}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'default':
      {'method': 'AROW', 'parameter': {'regularization_weight': 1.0}, 'converter': {'string_types': {'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}, 'unigram': {'method': 'ngram', 'char_num': '1'}}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'tf', 'global_weight': 'idf', 'type': 'bigram', 'key': '*'}]}}
    ,
    'euclidean':
      {'method': 'euclidean', 'parameter': {'nearest_neighbor_num': 16, 'local_sensitivity': 0.1}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'nherd':
      {'method': 'NHERD', 'parameter': {'regularization_weight': 1.0}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'nn':
      {'method': 'NN', 'parameter': {'nearest_neighbor_num': 128, 'method': 'euclid_lsh', 'parameter': {'hash_num': 64}, 'local_sensitivity': 1}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'pa':
      {'method': 'PA', 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'pa1':
      {'method': 'PA1', 'parameter': {'regularization_weight': 1.0}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'pa2':
      {'method': 'PA2', 'parameter': {'regularization_weight': 1.0}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'perceptron':
      {'method': 'perceptron', 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
  },
  ANOMALY: {
    'default':
      {'method': 'lof', 'parameter': {'nearest_neighbor_num': 10, 'method': 'inverted_index_euclid', 'reverse_nearest_neighbor_num': 30, 'parameter': {}, 'ignore_kth_same_point': True}, 'converter': {'string_types': {'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}, 'unigram': {'method': 'ngram', 'char_num': '1'}}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'tf', 'global_weight': 'idf', 'type': 'bigram', 'key': '*'}]}}
    ,
    'light_lof':
      {'method': 'light_lof', 'parameter': {'nearest_neighbor_num': 10, 'method': 'euclid_lsh', 'reverse_nearest_neighbor_num': 30, 'parameter': {'hash_num': 64}}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'light_lof_combinational_feature':
      {'method': 'light_lof', 'parameter': {'nearest_neighbor_num': 10, 'method': 'euclid_lsh', 'reverse_nearest_neighbor_num': 30, 'parameter': {'hash_num': 64}}, 'converter': {'string_types': {}, 'combination_rules': [{'key_left': '*', 'type': 'mul', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}], 'combination_types': {}}}
    ,
    'light_lof_unlearn_lru':
      {'method': 'light_lof', 'parameter': {'nearest_neighbor_num': 10, 'unlearner_parameter': {'max_size': 4096}, 'unlearner': 'lru', 'method': 'euclid_lsh', 'reverse_nearest_neighbor_num': 30, 'parameter': {'hash_num': 64}}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'lof':
      {'method': 'lof', 'parameter': {'nearest_neighbor_num': 10, 'method': 'euclid_lsh', 'reverse_nearest_neighbor_num': 30, 'parameter': {'probe_num': 64, 'hash_num': 64, 'bin_width': 100, 'table_num': 4, 'seed': 1091}}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'lof_inverted_index_euclid':
      {'method': 'lof', 'parameter': {'nearest_neighbor_num': 10, 'method': 'inverted_index_euclid', 'reverse_nearest_neighbor_num': 30, 'parameter': {}}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
    'lof_unlearner_lru':
      {'method': 'lof', 'parameter': {'nearest_neighbor_num': 10, 'unlearner_parameter': {'max_size': 4096}, 'unlearner': 'lru', 'method': 'euclid_lsh', 'reverse_nearest_neighbor_num': 30, 'parameter': {'probe_num': 64, 'hash_num': 64, 'bin_width': 100, 'table_num': 4, 'seed': 1091}}, 'converter': {'string_types': {}, 'num_filter_types': {}, 'num_rules': [{'type': 'num', 'key': '*'}], 'num_filter_rules': [], 'string_filter_rules': [], 'num_types': {}, 'string_filter_types': {}, 'string_rules': [{'sample_weight': 'bin', 'global_weight': 'bin', 'type': 'str', 'key': '*'}]}}
    ,
  },
}
