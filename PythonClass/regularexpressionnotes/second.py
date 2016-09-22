#!/usr/bin/python
import re
reg = re.compile('[a-z]+[-][a-z]+',re.I)
f = open('my_log.txt')
for value in f:
  m = reg.search(value)
  if m:
  #print m.group()
    print value[:m.start()] + value[m.end():]
  
