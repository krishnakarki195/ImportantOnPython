#!/usr/bin/python

version = 3.0

def my_add(a,b):
  ''' 
  The my_add function is for addition of strings and numbers. 
  '''
  return a + b
  
def my_sub(a,b):
  ''' This is going to substract the largest from smaller number'''
  if a > b:
    return a - b
  else:
    return b - a
    
# Main

if __name__ == '__main__':             # code below this line never get executed during import. Also function above this get imported.
  print "Launching the missile !!!"
    

