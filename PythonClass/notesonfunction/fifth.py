#!/usr/bin/python
# inner function gets defined during the runtime of upper function.
# inner is never available to us.

def upper():
  x = 1
  def inner():
    print x
  return inner()
  
upper()
inner()
  

