#!/usr/bin/python
import MySQLdb as mdb
con = mdb.connect('localhost','user46','user46','batch46') 
                #  server    , username,password,database
cur = con.cursor()
cur.executemany("insert into students (name,gender) values (%s,%s)",[('yugul','m')])
con.commit()
con.close()
