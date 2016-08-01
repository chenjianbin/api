#!/usr/bin/env python
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import sys


class Email(object):
	def __init__(self, sender, sender_pwd, from_user, to_user, smtp_host='smtp.exmail.qq.com', receivers=[], subject='报告', message='报告详情'):
		self.sender = sender
		self.sender_pwd = sender_pwd
		self.smtp_host = smtp_host
		self.receivers = receivers
		self.from_user = from_user
		self.to_user = to_user
		self.subject = subject
		self.message = message

	def format_message(self):
		message = MIMEText(self.message, 'html', 'utf-8')
		message['From'] = Header(self.from_user, 'utf-8')
		message['To'] =  Header(self.to_user, 'utf-8')
		message['Subject'] = Header(self.subject, 'utf-8')
		return message.as_string()

	def send():
		message = format_message()
		try:
			smtpobj = smtplib.SMTP(self.smtp_host)
			smtpobj.login(self.sender, self.sender_pwd)
			smtpobj.sendmail(self.sender, self.receivers, message)
			print('邮件发送成功')
		except smtplib.SMTPException:
			print('Error: 无法发送邮件')


if __name__ == '__main__':
	ins = Email(sender='xxxxxxx', sender_pwd='xxxxxxx', from_user='报告邮箱', to_user='运维负责人', smtp_host='smtp.exmail.qq.com', 
				receivers=[sys.argv[1]], subject=sys.argv[2], message=sys.argv[3])
	ins.send()
