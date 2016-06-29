#!/usr/bin/env python

class Config(object):
	DEBUG = True
	SECRET_KEY = 'development key'

class Database(Config):
	DBHOST = '127.0.0.1'
	DBPORT = 3306
	DBNAME = 'ops'
	DBUSER = 'ops'
	DBPASSWD = 'nbycm0fukZsdn1MG'

class Mail(Config):
	MAILHOST = 'smtp.exmail.qq.com'
	FROMADDR = 'send@wanjizhijia.com'
	TOADDR = ['ops@wanjizhijia.com', 'chenjianbin@wanjizhijia.com']
	SUBJECT = 'OPS APP ERROR !'
	MAILUSER = 'send@wanjizhijia.com'
	MAILPASSWD = 'BOZfdV8O2zMuTStp'
