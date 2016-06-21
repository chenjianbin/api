#!/usr/bin/env python
import urllib.request
import urllib.error
import aliyun.cdn.format_url as format_url

class Flush(object):
	def __init__(self, domain , files):
		self.domain = domain
		self.argsdict = {}
		self.argsdict['Action'] = 'RefreshObjectCaches'
		self.argsdict['ObjectType'] = 'File'
		self.files = files

	def run(self):
		for f in files:
			self.argsdict['ObjectPath'] = self.domain + '/' + f
			print('flush http://%s' % self.argsdict['ObjectPath'])
			ins = format_url.Format(self.argsdict) 
			url = ins.compose_url()
			try:
				with urllib.request.urlopen(url) as res:
					res = res.read().decode('utf-8')
			except urllib.error.HTTPError as res:
				res = str(res)
			finally:
				print(res)
					
