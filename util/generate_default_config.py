#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from os import path, listdir
import sys
import json

def line(indent=0, line='', out=sys.stdout):
  out.write('  ' * indent)
  out.write(line)
  out.write('\n')

def gen_header():
  line(0, '# -*- coding: utf-8 -*-')
  line()
  line(0, 'from __future__ import absolute_import, division, print_function, unicode_literals')
  line()

def gen_engine(e):
  line(0, e.upper() + ' = \'' + e + '\'')

def gen_engines_all(es):
  line()
  line(0, 'ALL_ENGINES = [' + ', '.join(map(str.upper, es)) + ']')
  line()

def gen_config(configs):
  line(0, 'CONFIGS = {')
  for (engine, record) in configs.items():
    line(1, engine.upper() + ': {')
    for (algorithm, config) in record:
      line(2, '\'' + algorithm + '\':')
      line(3, repr(config))
      line(2, ',')
    line(1, '},')
  line(0, '}')

def main(top_dir):
  configs = {}
  engines = sorted(listdir(top_dir))
  for engine in engines:
    configs[engine] = []
    for config in sorted(listdir(path.join(top_dir, engine))):
      (algorithm, _) = path.splitext(config)
      with open(path.join(top_dir, engine, config)) as f:
        configs[engine].append((algorithm, json.load(f)))

  gen_header()
  list(map(gen_engine, engines))
  gen_engines_all(engines)
  gen_config(configs)

if __name__ == '__main__':
  main(sys.argv[1])
