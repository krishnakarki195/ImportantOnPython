#!/usr/bin/python

'''
In [7]: map?
Type:       builtin_function_or_method
String Form:<built-in function map>
Namespace:  Python builtin
Docstring:
map(function, sequence[, sequence, ...]) -> list

Return a list of the results of applying the function to the items of
the argument sequence(s).  If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence, substituting None for missing values when not all
sequences have the same length.  If the function is None, return a list of
the items of the sequence (or a list of tuples if more than one sequence).

'''

def my_square(a):
  return a*a
  
print map(my_square,range(1,11)) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print filter(my_square,range(1,11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lambda : creation of functions on fly.
# lambda : nameless function
print map(lambda a: a * a,range(1,11))
print filter(lambda a:a * a,range(1,11))
  
  

