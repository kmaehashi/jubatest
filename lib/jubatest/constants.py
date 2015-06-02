# -*- coding: utf-8 -*-

"""
Provides default configurations for convenience
"""

import time
import copy

from .unit import JubaTestFixtureFailedError
from .logger import log

from ._jubatus_config import *

DEFAULT_CONFIG = {
  CLASSIFIER: 'perceptron',
  REGRESSION: 'pa',
  RECOMMENDER: 'inverted_index',
  STAT: 'stat',
  GRAPH: 'graph_wo_index',
  ANOMALY: 'lof',
  NEAREST_NEIGHBOR: 'lsh',
  CLUSTERING: 'kmeans',
  BURST: 'burst',
  BANDIT: 'epsilon_greedy',
}

def sleep(sec):
  log.debug('sleeping for %f seconds' % sec)
  time.sleep(sec)

def get_configs(engine):
  if engine in CONFIGS:
    return copy.deepcopy(CONFIGS[engine])
  raise JubaTestFixtureFailedError('no such engine: %s' % engine)

def default_config(engine):
  if engine in CONFIGS:
    return copy.deepcopy(CONFIGS[engine][DEFAULT_CONFIG[engine]])
  raise JubaTestFixtureFailedError('no such engine: %s' % engine)
