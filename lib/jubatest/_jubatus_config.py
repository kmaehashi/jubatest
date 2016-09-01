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
  CLASSIFIER: {
    'arow':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'AROW'}
    ,
    'arow_combinational_feature':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'combination_rules': [{'type': 'mul', 'key_left': '*', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'combination_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'AROW'}
    ,
    'cosine':
      {'parameter': {'nearest_neighbor_num': 16, 'local_sensitivity': 0.1}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'cosine'}
    ,
    'cw':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'CW'}
    ,
    'default':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'tf', 'key': '*', 'global_weight': 'idf', 'type': 'bigram'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {'unigram': {'method': 'ngram', 'char_num': '1'}, 'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}}}, 'method': 'AROW'}
    ,
    'euclidean':
      {'parameter': {'nearest_neighbor_num': 16, 'local_sensitivity': 0.1}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'euclidean'}
    ,
    'nherd':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'NHERD'}
    ,
    'nn':
      {'method': 'NN', 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'parameter': {'method': 'euclid_lsh', 'local_sensitivity': 1, 'nearest_neighbor_num': 128, 'parameter': {'hash_num': 64}}}
    ,
    'pa':
      {'method': 'PA', 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}}
    ,
    'pa1':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'PA1'}
    ,
    'pa2':
      {'parameter': {'regularization_weight': 1.0}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'PA2'}
    ,
    'perceptron':
      {'method': 'perceptron', 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}}
    ,
  },
  GRAPH: {
    'default':
      {'parameter': {'damping_factor': 0.9, 'landmark_num': 5}, 'method': 'graph_wo_index'}
    ,
    'graph_wo_index':
      {'parameter': {'damping_factor': 0.9, 'landmark_num': 5}, 'method': 'graph_wo_index'}
    ,
  },
  RECOMMENDER: {
    'default':
      {'method': 'inverted_index', 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'tf', 'key': '*', 'global_weight': 'idf', 'type': 'bigram'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {'unigram': {'method': 'ngram', 'char_num': '1'}, 'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}}}}
    ,
    'euclid_lsh':
      {'parameter': {'hash_num': 64, 'seed': 1091, 'bin_width': 100, 'table_num': 4, 'probe_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'euclid_lsh'}
    ,
    'euclid_lsh_unlearn_lru':
      {'parameter': {'hash_num': 64, 'seed': 1091, 'bin_width': 100, 'probe_num': 64, 'unlearner': 'lru', 'unlearner_parameter': {'max_size': 2048}, 'table_num': 4}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'euclid_lsh'}
    ,
    'inverted_index':
      {'method': 'inverted_index', 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}}
    ,
    'inverted_index_euclid':
      {'method': 'inverted_index_euclid', 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}}
    ,
    'inverted_index_euclid_unlearn_lru':
      {'parameter': {'unlearner': 'lru', 'unlearner_parameter': {'max_size': 2048}}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'inverted_index_euclid'}
    ,
    'inverted_index_unlearn_lru':
      {'parameter': {'unlearner': 'lru', 'unlearner_parameter': {'max_size': 2048}}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'inverted_index'}
    ,
    'lsh':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'lsh'}
    ,
    'lsh_combinational_feature':
      {'parameter': {'hash_num': 64}, 'converter': {'combination_rules': [{'type': 'mul', 'key_left': '*', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'combination_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'lsh'}
    ,
    'lsh_unlearn_lru':
      {'parameter': {'hash_num': 64, 'unlearner_parameter': {'max_size': 2048}, 'unlearner': 'lru'}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'lsh'}
    ,
    'minhash':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'minhash'}
    ,
    'minhash_unlearn_lru':
      {'parameter': {'hash_num': 64, 'unlearner_parameter': {'max_size': 2048}, 'unlearner': 'lru'}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'minhash'}
    ,
    'nearest_neighbor_recommender_euclid_lsh':
      {'parameter': {'method': 'euclid_lsh', 'parameter': {'hash_num': 512}}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'nearest_neighbor_recommender'}
    ,
    'nearest_neighbor_recommender_euclid_lsh_unlearn_lru':
      {'parameter': {'method': 'euclid_lsh', 'unlearner_parameter': {'max_size': 2048}, 'unlearner': 'lru', 'parameter': {'hash_num': 512}}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'nearest_neighbor_recommender'}
    ,
  },
  BURST: {
    'burst':
      {'parameter': {'max_reuse_batch_num': 5, 'window_batch_size': 5, 'costcut_threshold': -1, 'batch_interval': 10, 'result_window_rotate_size': 5}, 'method': 'burst'}
    ,
    'default':
      {'parameter': {'max_reuse_batch_num': 5, 'window_batch_size': 5, 'costcut_threshold': -1, 'batch_interval': 10, 'result_window_rotate_size': 5}, 'method': 'burst'}
    ,
  },
  ANOMALY: {
    'default':
      {'parameter': {'parameter': {}, 'method': 'inverted_index_euclid', 'nearest_neighbor_num': 10, 'reverse_nearest_neighbor_num': 30, 'ignore_kth_same_point': True}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'tf', 'key': '*', 'global_weight': 'idf', 'type': 'bigram'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {'unigram': {'method': 'ngram', 'char_num': '1'}, 'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}}}, 'method': 'lof'}
    ,
    'light_lof':
      {'parameter': {'method': 'euclid_lsh', 'nearest_neighbor_num': 10, 'reverse_nearest_neighbor_num': 30, 'parameter': {'hash_num': 64}}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'light_lof'}
    ,
    'light_lof_combinational_feature':
      {'parameter': {'method': 'euclid_lsh', 'nearest_neighbor_num': 10, 'reverse_nearest_neighbor_num': 30, 'parameter': {'hash_num': 64}}, 'converter': {'combination_rules': [{'type': 'mul', 'key_left': '*', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'combination_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'light_lof'}
    ,
    'light_lof_unlearn_lru':
      {'parameter': {'parameter': {'hash_num': 64}, 'nearest_neighbor_num': 10, 'unlearner': 'lru', 'method': 'euclid_lsh', 'unlearner_parameter': {'max_size': 4096}, 'reverse_nearest_neighbor_num': 30}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'light_lof'}
    ,
    'lof':
      {'parameter': {'method': 'euclid_lsh', 'nearest_neighbor_num': 10, 'reverse_nearest_neighbor_num': 30, 'parameter': {'hash_num': 64, 'seed': 1091, 'bin_width': 100, 'table_num': 4, 'probe_num': 64}}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'lof'}
    ,
    'lof_inverted_index_euclid':
      {'parameter': {'method': 'inverted_index_euclid', 'nearest_neighbor_num': 10, 'reverse_nearest_neighbor_num': 30, 'parameter': {}}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'lof'}
    ,
    'lof_unlearner_lru':
      {'parameter': {'parameter': {'hash_num': 64, 'seed': 1091, 'bin_width': 100, 'table_num': 4, 'probe_num': 64}, 'nearest_neighbor_num': 10, 'unlearner': 'lru', 'method': 'euclid_lsh', 'unlearner_parameter': {'max_size': 4096}, 'reverse_nearest_neighbor_num': 30}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'lof'}
    ,
  },
  WEIGHT: {
    'default':
      {'converter': {'binary_rules': [], 'num_filter_types': {'sigmoid': {'method': 'sigmoid_normalization', 'bias': '5', 'gain': '0.05'}, 'linear': {'min': '0', 'method': 'linear_normalization', 'max': '100'}, 'gaussian': {'method': 'gaussian_normalization', 'standard_deviation': '2.3', 'average': '80'}}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'tf', 'key': '*', 'global_weight': 'idf', 'type': 'unigram'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'binary_types': {}, 'num_filter_rules': [], 'string_types': {'unigram': {'method': 'ngram', 'char_num': '1'}, 'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}}}}
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
      {'parameter': {'forgetting_threshold': 0.5, 'bucket_length': 2, 'k': 3, 'bicriteria_base_size': 10, 'compressor_method': 'simple', 'compressed_bucket_size': 100, 'forgetting_factor': 0, 'seed': 0, 'bucket_size': 1000}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'tf', 'key': '*', 'global_weight': 'idf', 'type': 'bigram'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {'unigram': {'method': 'ngram', 'char_num': '1'}, 'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}}}, 'method': 'kmeans'}
    ,
    'gmm':
      {'parameter': {'forgetting_threshold': 0.5, 'bucket_length': 2, 'k': 3, 'bicriteria_base_size': 10, 'compressor_method': 'compressive_gmm', 'compressed_bucket_size': 100, 'forgetting_factor': 0, 'seed': 0, 'bucket_size': 1000}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'gmm'}
    ,
    'kmeans':
      {'parameter': {'forgetting_threshold': 0.5, 'bucket_length': 2, 'k': 3, 'bicriteria_base_size': 10, 'compressor_method': 'compressive_kmeans', 'compressed_bucket_size': 100, 'forgetting_factor': 0, 'seed': 0, 'bucket_size': 1000}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'kmeans'}
    ,
    'kmeans_combinational_feature':
      {'parameter': {'forgetting_threshold': 0.5, 'bucket_length': 2, 'k': 3, 'bicriteria_base_size': 10, 'compressor_method': 'compressive_kmeans', 'compressed_bucket_size': 100, 'forgetting_factor': 0, 'seed': 0, 'bucket_size': 1000}, 'converter': {'combination_rules': [{'type': 'mul', 'key_left': '*', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'combination_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'kmeans'}
    ,
  },
  REGRESSION: {
    'default':
      {'parameter': {'regularization_weight': 3.402823e+38, 'sensitivity': 0.1}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'tf', 'key': '*', 'global_weight': 'idf', 'type': 'bigram'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {'unigram': {'method': 'ngram', 'char_num': '1'}, 'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}}}, 'method': 'PA'}
    ,
    'pa':
      {'parameter': {'regularization_weight': 3.402823e+38, 'sensitivity': 0.1}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'PA'}
    ,
    'pa_combinational_feature':
      {'parameter': {'regularization_weight': 3.402823e+38, 'sensitivity': 0.1}, 'converter': {'combination_rules': [{'type': 'mul', 'key_left': '*', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'combination_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'PA'}
    ,
  },
  NEAREST_NEIGHBOR: {
    'default':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'tf', 'key': '*', 'global_weight': 'idf', 'type': 'bigram'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {'unigram': {'method': 'ngram', 'char_num': '1'}, 'bigram': {'method': 'ngram', 'char_num': '2'}, 'trigram': {'method': 'ngram', 'char_num': '3'}}}, 'method': 'lsh'}
    ,
    'euclid_lsh':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'euclid_lsh'}
    ,
    'lsh':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'lsh'}
    ,
    'lsh_combinational_feature':
      {'parameter': {'hash_num': 64}, 'converter': {'combination_rules': [{'type': 'mul', 'key_left': '*', 'key_right': '*'}], 'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'combination_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'lsh'}
    ,
    'lsh_multithread':
      {'parameter': {'threads': 2, 'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'lsh'}
    ,
    'minhash':
      {'parameter': {'hash_num': 64}, 'converter': {'num_filter_types': {}, 'num_rules': [{'key': '*', 'type': 'num'}], 'string_rules': [{'sample_weight': 'bin', 'key': '*', 'global_weight': 'bin', 'type': 'str'}], 'string_filter_types': {}, 'num_types': {}, 'string_filter_rules': [], 'num_filter_rules': [], 'string_types': {}}, 'method': 'minhash'}
    ,
  },
}
