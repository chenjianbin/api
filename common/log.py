#!/usr/bin/env python
import flask
import logging

app = flask.Flask(__name__)
app.config.from_object('config.config.Mail')

class SendMail(object):
	def __init__(self):
		self.mailhost = app.config.get('MAILHOST')
		self.fromaddr = app.config.get('FROMADDR')
		self.toaddr = app.config.get('TOADDR')
		self.subject = app.config.get('SUBJECT')
		self.mailuser = app.config.get('MAILUSER')
		self.mailpasswd = app.config.get('MAILPASSWD')

	def switch(self, status=False):
		if not status:
			mail_handler = logging.handlers.SMTPHandler(self.mailhost, self.fromaddr, self.toaddr, self.subject, (self.mailuser, self.mailpasswd))
			mail_handler.setLevel(logging.ERROR)
			app.logger.addHandler(mail_handler)
			
