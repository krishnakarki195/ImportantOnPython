#!/usr/bin/python
# function are first class objects.

def add(x,y):
  return x + y
  
def sub(x,y):
  return x - y
  
def extra(func,x,y):
  return func(x,y)
  
print extra(add,10,20) # add is acting like anyother object - int,string,float
print extra(sub,40,30)
