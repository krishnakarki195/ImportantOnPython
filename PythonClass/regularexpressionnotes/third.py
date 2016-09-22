#!/usr/bin/python
import re
reg = re.compile('[a-z0-9.]+@[a-z.]+')
emails = open('email.txt')
email_dump = emails.read()
print reg.findall(email_dump)
#print email_dump

