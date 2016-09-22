#!/usr/bin/python
# exception module 
# import exception => class Exception

class InvalidAgeException(Exception):
    def __init__(self,age):
      self.age = age
  
def validate_age(age):
  if age < 18:
    raise InvalidAgeException(age)

# Main  
age = int(raw_input("please enter the age:"))
try:
  validate_age(age)
except InvalidAgeException as e:
  print "buddy!! you are too young for the movie {}".format(e.age)
else:
  print "buddy!! you are eligible to watch the movie"
