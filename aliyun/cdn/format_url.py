#!/usr/bin/env python
#-- coding:utf-8 --
import os
import urllib.parse
import configparser
import uuid
import time
import hmac
import hashlib
import base64

CONFIGFILE = os.path.split(os.path.realpath(__file__))[0] + '/' + '../../config/aliyun.ini'
CONFIGSECTION = 'cdn'

CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIGFILE)
SERVERADDRESS = CONFIG.get(CONFIGSECTION, 'serveraddress')
ACCESSKEYSECRET = CONFIG.get('key', 'accesskeysecret')

'''
对请求的URL进行签名以及编码
参考https://help.aliyun.com/document_detail/27149.html?spm=5176.doc27200.6.139.paDf9R
'''
class Format(object):
	def __init__(self,args):
		self.argsdict = {}
		self.argsdict['TimeStamp'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
		self.argsdict['SignatureNonce'] = str(uuid.uuid1())
		self.argsdict['AccessKeyId'] = CONFIG.get('key', 'accesskeyid')
		self.argsdict['Format'] = CONFIG.get(CONFIGSECTION, 'format')
		self.argsdict['Version'] = CONFIG.get(CONFIGSECTION, 'version')
		self.argsdict['SignatureVersion'] = CONFIG.get(CONFIGSECTION, 'signatureversion')
		self.argsdict['SignatureMethod'] = CONFIG.get(CONFIGSECTION, 'signaturemethod')
		for key in args.keys():
			self.argsdict[key] = args[key]

	def compose_url(self): 
		signature = self.compute_signature(self.argsdict, ACCESSKEYSECRET)
		self.argsdict['Signature'] = signature
		url = SERVERADDRESS + "/?" + urllib.parse.urlencode(self.argsdict, safe='/')
		return url

	def compute_signature(self, parameters, access_key_secret):
		sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
		canonicalizedQueryString = ''
		for (k,v) in sortedParameters:
			canonicalizedQueryString += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)

		stringToSign = 'GET&%2F&' + self.percent_encode(canonicalizedQueryString[1:])

		key = access_key_secret + '&'
		h = hmac.new(key.encode('utf-8'), stringToSign.encode('utf-8'), hashlib.sha1)
		signature = base64.encodestring(h.digest()).strip()
		return signature
	
	def percent_encode(self, argument):
		res = urllib.parse.quote_plus(argument)
		res = res.replace('%7E', '~')
		return res
		
