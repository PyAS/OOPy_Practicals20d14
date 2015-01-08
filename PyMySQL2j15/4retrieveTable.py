#!/usr/bin/python
# _*_ coding: utf-8 _*_

import MySQLdb as mdb

con = mdb.connect('localhost','testuser','test623','testdb');

with con:

	cur = con.cursor()
	cur.execute("SELECT * FROM Writers")
	
	rows = cur.fetchall()

	for row in rows:
		print row
