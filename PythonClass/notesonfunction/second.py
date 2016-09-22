#!/usr/bin/python
# scope

# local scope
# the variable created inside the function are restricted to the function.
# scope resolution: if a value is not present locally, we will try searching it globally.
# scope resolution : the local scope is given higher precedence than global scope.
# global

x = 10

def my_func():
  global x
  print locals()
  x = x + 1
  return x
  
print globals()
print my_func()


'''
# example 3

x = 10   # global variable

def my_func():
  x = 1
  print locals()
  return x
  
print globals()
print my_func()


# example 2:


x = 10   # global variable

def my_func():
  print locals()
  return x
  
print globals()
print my_func()

# example 1:

def my_func():
  x = 1
  return locals()
  
print my_func()
print x

{'x': 1}
Traceback (most recent call last):
  File "second.py", line 11, in <module>
    print x
NameError: name 'x' is not defined
'''

