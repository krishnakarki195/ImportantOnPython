#!/usr/bin/python
'''
In [11]: filter?
Type:       builtin_function_or_method
String Form:<built-in function filter>
Namespace:  Python builtin
Docstring:
filter(function or None, sequence) -> list, tuple, or string

Return those items of sequence for which function(item) is true.  If
function is None, return the items that are true.  If sequence is a tuple
or string, return the same type, else return a list.
'''

def my_even(a):
  if a % 2 == 0:
    return 'even'
    
print filter(my_even,range(1,11)) # [2, 4, 6, 8, 10]
print map(my_even,range(1,11))    # [None, 'even', None, 'even', None, 'even', None, 'even', None, 'even']


# Lambda : creation of functions on fly.
# lambda : nameless function
print map(lambda a: a % 2 == 0,range(1,11)) # [False, True, False, True, False, True, False, True, False, True]
print filter(lambda a: a % 2 == 0,range(1,11)) # [2, 4, 6, 8, 10]
