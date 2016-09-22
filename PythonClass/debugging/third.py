#!/usr/bin/python
import pdb

def first():
  second()
  print "i am in the first function"

def second():
  third()
  print "i am in the second function"
  
def third():
  fourth()
  print "i am in the third function"
  
def fourth():
  fifth()
  print "i am in the fourth function"
  
def fifth():
  print "i am in the fifth function"
  
pdb.set_trace()
first()
















