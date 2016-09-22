#!/usr/bin/python
# inheritance

# salried people
class account:
  def __init__(self):
    self.balance = 0
  def deposit(self,amount):
    self.balance = self.balance + amount
    return self.balance
  def withdraw(self,amount):
    self.balance = self.balance - amount
    return self.balance
    
    
class MinBalanceAccount(account):
  def __init__(self):
    account.__init__(self)
    self.mimamount=1000
  def withdraw(self,amount):
    if self.balance - amount < self.mimamount:
      print "buddy you balance is low"
    else:
      account.withdraw(self,amount)
      
# yugul - employeed, san - student

# yugul
yugul = account()
print "Initial balance of yugul {}".format(yugul.balance)
yugul.deposit(2000)
print "After deposit balance yugul {}".format(yugul.balance)
yugul.withdraw(2500)
print "after withdrawal balance of yugul {}".format(yugul.balance)

# san
san = MinBalanceAccount()
print "Initial balance of san {}".format(san.balance)
print "minium balance to be kept {}".format(san.mimamount)
san.deposit(2000)
print "After deposit balance of san {}".format(san.balance)
san.withdraw(1000)
print "after withdrawal balance of san {}".format(san.balance)
san.withdraw(1000)
print "after withdrawal balance of san {}".format(san.balance)

    
