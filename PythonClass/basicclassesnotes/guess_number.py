#!/usr/bin/python
# guess my number
# break : break will take you out of the loop but still inside the program.
# sys.exit : take you completly out of the program.

import sys
answer = raw_input("do you really want to play the game:y/n: ")
if answer == 'n':
  sys.exit() 

number = 7
#test = True

while True:
  guess = int(raw_input("please guess the number:"))
  if guess > number:
    print "your {} is greater than number".format(guess)
  elif guess < number:
    print "your {} is lesser than number".format(guess)
  elif guess == number:
    print "hurray!!! you got the right number"
    break
    #test=False
    

print "thanks for playing the game"
    
