#!/usr/bin/python

def account():
  return {'balance':0}
  
def deposit(account,amount):
  account['balance'] = account['balance'] + amount
  return account['balance']
  
def withdraw(account,amount):
  account['balance'] = account['balance'] - amount
  return account['balance']
  
# san
san = account()
print "Initial balance of san {}".format(san['balance'])
deposit(san,1000)
print "After deposit balance of san {}".format(san['balance'])
withdraw(san,500)
print "after withdrawal balance of san {}".format(san['balance'])

# yugul
yugul = account()
print "Initial balance of yugul {}".format(yugul['balance'])
deposit(yugul,2000)
print "After deposit balance yugul {}".format(yugul['balance'])
withdraw(yugul,500)
print "after withdrawal balance of yugul {}".format(yugul['balance'])
