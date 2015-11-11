# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import logging

log = logging.getLogger('jubatest')

def setup_logger(log_level, log_file):
    log.propagate = False

    if not log_level:
        return

    if log_file:
        f = open(log_file, 'w')
    else:
        f = sys.stderr

    handler = logging.StreamHandler(f)
    formatter = logging.Formatter('%(asctime)s:%(name)s[%(thread)d]:%(filename)s:%(lineno)d:%(funcName)s:%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(log_level)
    log.debug('logger initialized, level set to %s', log_level)
