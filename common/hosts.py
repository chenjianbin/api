#!/usr/bin/env python
#-- coding:utf-8 --
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('config/site.conf')

class Hosts(object):
	def __init__(self, domain):
		self.domain = domain
	
	def get(self):
		'''
		获取站点所在服务器IP列表
		'''
		hosts = CONFIG.get('hosts', self.domain).split(',')
		return hosts
		
