#!/usr/bin/python
# _*_ coding: utf-8 _*_

import MySQLdb as mdb
import sys

try:
	con = mdb.connect('localhost','testuser', 'test623','testdb')

	cur = con.cursor()
	cur.execute("SELECT VERSION()")
	
	ver = cur.fetchone()
	
	print "DataBase version: %s" % ver

except mbd.Error,e:

	print "Error %d: %s" % (e.args[0],e.args[1])
	sys.exit(1)

finally:
	if con:
		con.close()
