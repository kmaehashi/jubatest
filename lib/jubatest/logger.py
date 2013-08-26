# -*- coding: utf-8 -*-

import logging

log = logging.getLogger('jubatest')

def setup_logger(log_level):
    log.propagate = False

    if not log_level:
        return

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s:%(name)s[%(thread)d]:%(filename)s:%(lineno)d:%(funcName)s:%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(log_level)
    log.debug('logger initialized, level set to %s', log_level)
