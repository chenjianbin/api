#!/usr/bin/env python
#-- coding:utf-8 --
''' manage aliyun cdn '''

import urllib.request
import configparser
import uuid
import time

CONFIGFILE = '../../config/aliyun.conf'
CONFIGSECTION = 'cdn'

config = configparser.ConfigParser()
config.read(CONFIGFILE)
ACCESSKEYID = config.get('key', 'accesskeyid')
ACCESSKEYSECRET = config.get('key', 'accesskeysecret')
ServerAddress = config.get(CONFIGSECTION, 'serveraddress')
FORMAT = config.get(CONFIGSECTION, 'format')
SIGNATUREVERSION = config.get(CONFIGSECTION, 'signatureversion')
SIGNATUREMOTHOD = config.get(CONFIGSECTION, 'signaturemethod')


class FormatURL():
	def __init__(self,args):
		
	
