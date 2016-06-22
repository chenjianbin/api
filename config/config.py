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
