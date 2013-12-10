# -*- coding: utf-8 -*-

"""
Provides default configurations for convenience
"""

import time
import copy

from .unit import JubaTestFixtureFailedError
from .logger import log


CLASSIFIER = 'classifier'
REGRESSION = 'regression'
RECOMMENDER = 'recommender'
STAT = 'stat'
GRAPH = 'graph'
ANOMALY = 'anomaly'
NEAREST_NEIGHBOR = 'nearest_neighbor'
CLUSTERING = 'clustering'

def sleep(sec):
    log.debug('sleeping for %f seconds' % sec)
    time.sleep(sec)

def default_config(engine):
    if engine in _ConfigHolder.default:
        return copy.deepcopy(_ConfigHolder.default.get(engine))
    raise JubaTestFixtureFailedError('no such engine: %s' % engine)

class _ConfigHolder(object):
    _converter = {
        "string_filter_types": {},
        "string_filter_rules": [],
        "num_filter_types": {},
        "num_filter_rules": [],
        "string_types": {},
        "string_rules": [{"key": "*", "type": "str",  "sample_weight": "bin", "global_weight": "bin"}],
        "num_types": {},
        "num_rules": [{"key": "*", "type": "num"}],
        "binary_types": {},
        "binary_rules": []
    }
    default = {
        CLASSIFIER: {
            "method": "perceptron",
            "converter": _converter,
            "parameter": {
                "regularization_weight": 1.0
            }
        },
        REGRESSION: {
            "method": "PA",
            "converter": _converter,
            "parameter": {
                "sensitivity" : 0.1,
                "regularization_weight" : 3.402823e+38
            }
        },
        RECOMMENDER: {
            "method": "inverted_index",
            "converter": _converter
        },
        ANOMALY: {
         "method": "lof",
         "converter" : _converter,
         "parameter": {
           "nearest_neighbor_num": 10,
           "reverse_nearest_neighbor_num": 30,
           "method": "euclid_lsh",
           "parameter": {
             "hash_num": 64,
             "table_num": 4,
             "seed": 1091,
             "probe_num": 64,
             "bin_width": 100,
             "retain_projection": False
           }
         }
        },
        GRAPH: {
            "method": "graph_wo_index",
            "parameter": {
                "damping_factor": 0.9,
                "landmark_num": 5
            }
        },
        STAT: {
            "window_size": 128
        },
        NEAREST_NEIGHBOR: {
            "method" : "kmeans",
            "converter": _converter,
            "parameter" : {
              "k" : 3,
              "compressor_method" : "compressive_kmeans",
              "bucket_size" : 1000,
              "compressed_bucket_size" : 100,
              "bicriteria_base_size" : 10,
              "bucket_length" : 2,
              "forgetting_factor" : 0,
              "forgetting_threshold" : 0.5
            }
        },
        CLUSTERING: {
            "method": "lsh",
            "parameter" : {
                "hash_num" : 64
            }
        }
    }
