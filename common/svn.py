#!/usr/bin/env python
#-- coding:utf-8 --
import common.ssh
import configparser
import os
import re


class Svn(object):
	def __init__(self, host, dirname, site):
		self.host = host
		self.dirname = dirname
		self.site = site

	def update(self):
		'''
		更新线上代码
		'''
		command = 'svn update %s/%s ' % (self.dirname, self.site)
		ssh = common.ssh.SSHClient(self.host, command)
		return ssh.execute()

	def get_diff_files(self):
		'''
		获取两个git版本的差异文件列表
		'''
		command = 'svn update %s/%s -r HEAD -v' % (self.dirname, self.site)
		ssh = common.ssh.SSHClient(self.host, command)
		return ssh.execute()

	def get_m_files(self):
		configfile = os.path.split(os.path.realpath(__file__))[0] + '/' + '../config/aliyun.ini'
		config = configparser.ConfigParser()
		config.read(configfile)
		filetypes = config.get('cdn', 'filetypes')
		stdout, stderr = self.get_diff_files()
		files = []
		for i in stdout:
			if re.match('\s*M.*?\.%s' % filetypes, i):
				files.append(i[1:].strip())
		return files
		
