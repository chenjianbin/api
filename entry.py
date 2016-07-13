#!/usr/bin/env python
from flask import Flask, render_template
import language.php
import logging
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config.config.Database')
app.config.from_object('config.config.Mail')
Bootstrap(app)

app.debug = False
@app.route('/login', methods=['GET', 'POST'])
def login():
	pass

@app.route('/release/<domain>')
def release(domain):
	ins = language.php.Update(domain)
	res = ins.run()
	app.logger.info('An error occurred')
	return res

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

class Log(object):
	def __init__(self):
		self.mailhost = app.config.get('MAILHOST')
		self.fromaddr = app.config.get('FROMADDR')
		self.toaddr = app.config.get('TOADDR')
		self.subject = app.config.get('SUBJECT')
		self.mailuser = app.config.get('MAILUSER')
		self.mailpasswd = app.config.get('MAILPASSWD')

	def switch(self, status=False):
		if status:
			import logging.handlers
			mail_handler = logging.handlers.SMTPHandler(self.mailhost, self.fromaddr, self.toaddr, self.subject, credentials=(self.mailuser, self.mailpasswd))
			mail_handler.setLevel(logging.DEBUG)
			mail_handler.setFormatter(logging.Formatter('''
			Message type:       %(levelname)s
			Location:           %(pathname)s:%(lineno)d
			Module:             %(module)s
			Function:           %(funcName)s
			Time:               %(asctime)s

			Message:

			%(message)s
			'''))
			file_handler = logging.FileHandler('logs/test.log', mode='a', encoding='utf8')
			file_handler.setLevel(logging.DEBUG)
			file_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s ''[in %(pathname)s:%(lineno)d]'))
			app.logger.addHandler(mail_handler)
			app.logger.addHandler(file_handler)
			

if __name__ == '__main__':
	ins = Log()
	print('111')
	ins.switch(status=True)
	app.run(host='0.0.0.0', port=81)
