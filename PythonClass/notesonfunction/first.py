#!/usr/bin/python

def my_func():
  return "hello world"
  print "one"
  print "two"
  print "three"
  
print type(my_func)
print my_func
print my_func()

# return is not a print statement. Return marks the end of the function.
# if today is tuesday:
#   return
# else
#   return 


'''
def my_func():
  print "hello world"
  
print type(my_func)
print my_func
print my_func()

<type 'function'>
<function my_func at 0x7ff73940a5f0>
hello world
None
# every function has  a return value.
'''
