#!/usr/bin/python

import MySQLdb as mdb
con = mdb.connect('localhost','user46','user46','batch46') 
                #  server    , username,password,database
cur = con.cursor()
cur.execute("select user()")
user = cur.fetchone()[0].split('@')[0]
print "I am currently logged in a user - {}".format(user)

