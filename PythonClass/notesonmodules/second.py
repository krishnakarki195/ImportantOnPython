#!/usr/bin/python

import sys
sys.path.insert(0,'/home/tuxfux-hlp/Desktop/batch-46/modules/extra')

import first as f

def my_add(a,b):
  ''' this function is for addition of intergers '''
  a = int(a)
  b = int(b)
  return a + b
  
# Main
if __name__ == '__main__':
  print "addition of two numbers is {} ".format(my_add(10,20))
  print "addition of two strings is {}".format(f.my_add('today',' rocks'))
  
