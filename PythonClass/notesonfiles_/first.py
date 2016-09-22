#!/usr/bin/python
from excel import OpenExcel
f = OpenExcel('namesdb.xls')
#name = raw_input("please enter the name of the student:")
print f.read('A') # read 'A' row
print f.read('A7'),f.read('B7') # read 'A' row

