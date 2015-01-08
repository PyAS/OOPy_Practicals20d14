#!/usr/bin/python
# _*_ coding: utf-8 _*_

import MySQLdb as mdb
import sys

try:
	con = mdb.connect('localhost','testuser','test623','testdb')

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Writers")
	cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
	cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
	cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
	cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
	cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
	cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
	cur.execute("INSERT INTO Writers(Name) VALUES('Terry Pratchett')")

	con.commit()

except mdb.Error,e:
	if con:
		con.rollback()

	print "Error %d: %s" % (e.args[0],e.args[1])
	sys.exit()

finally:
	if con:
		con.close()


