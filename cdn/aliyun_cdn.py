#!/usr/bin/env python
#-- coding:utf-8 --
''' manage aliyun cdn '''

import urllib.request
import configparser
import uuid

config = configparser.ConfigParser()
config.read('../config/aliyun.conf')
URL = config.get('cdn','url')
FORMAT = config.get('cdn','format')
ACCESSKEYID = config.get('cdn','accesskeyid')
ACCESSKEYSECRET = config.get('cdn','accesskeysecret')
SIGNATUREVERSION = config.get('cdn','signatureversion')
SIGNATUREMOTHOD = config.get('cdn','signaturemethod')


def Flush():
    #with urllib.request.openurl() as f:
     #   print (f.read())
	pass
