#!/usr/bin/python

class account:
  def __init__(self):
    self.balance = 0
  def deposit(self,amount):
    self.balance = self.balance + amount
    return self.balance
  def withdraw(self,amount):
    self.balance = self.balance - amount
    return self.balance
    
# san
san = account()
print "Initial balance of san {}".format(san.balance)
san.deposit(1000)
print "After deposit balance of san {}".format(san.balance)
san.withdraw(1500)
print "after withdrawal balance of san {}".format(san.balance)

# yugul
yugul = account()
print "Initial balance of yugul {}".format(yugul.balance)
yugul.deposit(2000)
print "After deposit balance yugul {}".format(yugul.balance)
yugul.withdraw(500)
print "after withdrawal balance of yugul {}".format(yugul.balance)

