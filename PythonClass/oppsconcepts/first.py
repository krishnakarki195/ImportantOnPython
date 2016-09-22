#!/usr/bin/python
balance = 0

def deposit(amount):
  global balance
  balance = balance + amount
  return balance
  
def withdraw(amount):
  global balance
  balance = balance - amount
  return balance
 
# san
 
print "my initial amount for san {}".format(balance)
deposit(1000)
print "After deposit my amount for san {}".format(balance)
withdraw(200)
print "After withdraw my amount for san {}".format(balance)

# yugul

print "my initial amount for yugul {}".format(balance)
