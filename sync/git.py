#!/usr/bin/env python
#-- coding:utf-8 --
import common.ssh
import configparser
import os
import re


class Git(object):
	def __init__(self, host, dirname, site):
		self.host = host
		self.dirname = dirname
		self.site = site

	def pull(self):
		'''
		更新线上代码
		'''
		command = 'cd %s%s && git pull' % (self.dirname, self.site)
		ssh = common.ssh.SSHClient(self.host, command)
		return ssh.execute()

	def get_diff_files(self, version_old='HEAD~', version_new='HEAD'):
		'''
		获取两个git版本的差异文件列表
		'''
		#configfile = os.path.split(os.path.realpath(__file__))[0] + '/' + '../config/aliyun.conf'
		#config = configparser.ConfigParser()
		#config.read(configfile)
		#filetypes = config.get('cdn', 'filetypes')
		command = 'cd %s%s && git diff-tree -r --name-status --no-commit-id %s %s' % (self.dirname, self.site, version_old, version_new)
		ssh = common.ssh.SSHClient(self.host, command)
		return ssh.execute()

	def get_m_files(self, version_old='HEAD~', version_new='HEAD'):
		configfile = os.path.split(os.path.realpath(__file__))[0] + '/' + '../config/aliyun.ini'
		config = configparser.ConfigParser()
		config.read(configfile)
		filetypes = config.get('cdn', 'filetypes')
		stdout, stderr = self.get_diff_files(version_old=version_old, version_new=version_new)
		files = []
		for i in stdout:
			if re.match('M.*?\.%s' % filetypes, i):
				files.append(i[1:].strip())
		return files
		
