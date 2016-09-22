#!/usr/bin/python
# Functionn decoraation - decorator

def upper():
  x = 1
  def inner():
    print x
  return inner  # Label of function inner
  
foo = upper()
print type(foo)
print foo
foo()

# function enclosures
# if your function is using any variables during the runtime, it stays with the function.


