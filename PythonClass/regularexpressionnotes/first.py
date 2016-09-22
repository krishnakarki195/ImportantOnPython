#!/usr/bin/python
import re

answer = raw_input("do you want to come to cinema? - yes/no : ")
#if answer == 'yes':
if re.match(answer,'yes',re.I):
  print "please come to cinema by 7.00"
else:
  print "Lets go to movie next time"
