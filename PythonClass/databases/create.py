import MySQLdb as mdb
con = mdb.connect('localhost','user46','user46','batch46') 
                #  server    , username,password,database
cur = con.cursor()
cur.execute("create table students (name varchar(10),gender varchar(6))")
con.close()
