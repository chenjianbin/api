#!/usr/bin/env python
import flask
import MySQLdb
import time
import contextlib

app = flask.Flask(__name__)
app.config.from_object('config.config.Database')
DBHOST = app.config['DBHOST']
DBPORT = app.config['DBPORT']
DBUSER = app.config['DBUSER']
DBPASSWD = app.config['DBPASSWD']
DBNAME = app.config['DBNAME']

def db_connect():
	return MySQLdb.connection(host=DBHOST, port=DBPORT, user=DBUSER, passwd=DBPASSWD, db=DBNAME)

@app.route('/login', methods=['GET', 'POST'])
def login():
	pass

@app.route('/test')
def test():
	with contextlib.closing(db_connect()) as db:
		db.query("select sleep(10)")
		time.sleep(10)
		return "wanle"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
