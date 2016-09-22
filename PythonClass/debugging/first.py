#!/usr/bin/python
# pdb.set_trace
# to start coding from anywhere.

import pdb

version=1.0

def my_add(a,b):
  print "value of a is {}".format(a)
  print "value of b is {}".format(b)
  result = a + b
  return result

def my_sub(a,b):
  if a > b:
    return a - b
  else:
    return b - a

def my_div(a,b=1):
  return a/b

def my_multi(a,b):
  return a * b

if __name__ == '__main__':
  print "welcome to the debugging classes."
  print "i can skip the 24 and 25 line."
  pdb.set_trace()
  print "addition of two numbers {}".format(my_add(1,4))
  print "substraction of two numbers {}".format(my_sub(10,20))
  print "division of two numbers {}".format(my_div(10,2))
  print "multiplication of two numbers {}".format(my_multi(10,2))
