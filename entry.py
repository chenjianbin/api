#!/usr/bin/env python
import flask
import common.mysql
import json

app = flask.Flask(__name__)
app.config.from_object('config.config.Database')

@app.route('/login', methods=['GET', 'POST'])
def login():
	pass

@app.route('/release/<domain>')
def release(domain):
	cmd = '''select * from  re_site where id=%s'''
	args = ('1')
	con = common.mysql.Connect()
	res = json.loads(con.execute(cmd, args))
	return res
	#a = dict(res)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=81)
