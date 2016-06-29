#!/usr/bin/env python
import MySQLdb
import contextlib
import flask
import json

app = flask.Flask(__name__)
app.config.from_object('config.config.Database')
DBHOST = app.config.get('DBHOST')
DBPORT = app.config.get('DBPORT')
DBUSER = app.config.get('DBUSER')
DBPASSWD = app.config.get('DBPASSWD')
DBNAME = app.config.get('DBNAME')

class Connect(object):
	def __init__(self):
		self.connect = MySQLdb.connect(host=DBHOST, port=DBPORT, user=DBUSER, passwd=DBPASSWD, db=DBNAME)

	def execute(self, cmd, *args_tuple):
		with contextlib.closing(self.connect) as con:
			with con.cursor(MySQLdb.cursors.DictCursor) as cur:
				cur.execute(cmd, args_tuple)
				res = cur.fetchall()
				con.commit()
				return json.dumps(res)
