#!/usr/bin/python
# try .. except .. else .. finally
# try : computation parts
# except : exception handling.
# else : when your try is True
# finally:
# case 1: All valid values .. try - else - finally.
# case 2: Invalid values .. Handled by exceptions .. try - except - finally.
# case 3: Invalid values .. Exception handling not taken care .. try - finally - Bomd with exception.

# example 5

try:
  num1 = int(raw_input("please enter the number 1:"))
  num2 = int(raw_input("please enter the number 2:"))
  result = num1/num2
except ValueError:
  print "please make sure you enter numbers. "
else:
  print result
finally:
  print "close all the connections"



'''
# example 4
try:
  num1 = int(raw_input("please enter the number 1:"))
  num2 = int(raw_input("please enter the number 2:"))
  result = num1/num2
except ValueError,error:
  print "please make sure you enter numbers. "
  print error
except ZeroDivisionError,error:
  print "Please make sure your denominator is non-zero."
  print error
else:
  print result



# example 3
try:
  num1 = int(raw_input("please enter the number 1:"))
  num2 = int(raw_input("please enter the number 2:"))
  result = num1/num2
except ValueError:
  print "please make sure you enter numbers. "
except ZeroDivisionError:
  print "Please make sure your denominator is non-zero."
else:
  print result



# example 2
try:
  num1 = int(raw_input("please enter the number 1:"))
  num2 = int(raw_input("please enter the number 2:"))
  result = num1/num2
except (ValueError,ZeroDivisionError):
  print "please make sure you enter numbers. Please make sure your denominator is non-zero"
else:
  print result


# example 1

try:
  num1 = int(raw_input("please enter the number 1:"))
  num2 = int(raw_input("please enter the number 2:"))
  result = num1/num2
except:
  print "please make sure you enter numbers. Please make sure your denominator is non-zero"
else:
  print result
'''
