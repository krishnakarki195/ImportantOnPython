#!/usr/bin/python
# functional arguments
# pass by value or pass by reference -> pass by object

'''
def add(a,b):
  print locals()
  return a + b
  
print add(10,20)
print add("linux"," rocks")
print add(b=' linux',a='rocks')

# you can pass object on position or using key values.
'''

# default keyvalues - Note: default is not a keyword
# multiplication table.
def multi(num,default=10):
  for value in range(1,default+1):
    print "{0:2d} * {1:2d} = {2:3d}".format(num,value,num*value)
    
#multi(2)
# multi(2,20)
multi(default=20,num=3)
# def putty(hostname,port=22)
# putty(hostname) => ssh port
# putty(hostname,23) => telnet port
  
