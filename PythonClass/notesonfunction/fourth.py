#!/usr/bin/python
# *,**,*args(args),**kwargs(kwargs)

def callguy(**kwargs):
  if 'name' in kwargs:
    print kwargs['name']
  if 'age' in kwargs:
    print kwargs['age']
  if 'gender' in kwargs:
    print kwargs['gender']
  if 'email' in kwargs:
    print kwargs['email']
  

callguy(name='kushi',age=1)
#callguy(age=1,gender='f')
#callguy(name='kushi',email='kushi.hlp@gmail.com')




'''
def gmax(*args):
  big=0
  for value in args:
    if value > big:
      big = value
  return big
  
print gmax(21,42,55,98,99,1)




In [3]: max?
Type:       builtin_function_or_method
String Form:<built-in function max>
Namespace:  Python builtin
Docstring:
max(iterable[, key=func]) -> value
max(a, b, c, ...[, key=func]) -> value

With a single iterable argument, return its largest item.
With two or more arguments, return the largest argument.

In [4]: max(21,42)
Out[4]: 42

In [5]: max(21,42,55,98,99,01)
Out[5]: 99



def my_func(a,b):
  return a + b

# my_func(10,20)  
my_list = [1,2]
print my_func(*my_list)

my_dict = {'b':10,'a':10}
print my_func(**my_dict)
'''
