#!/usr/bin/env python
#-- coding:utf-8 --
import common.ssh
import configparser
import os


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
		获取修改过的文件列表
		'''
		configfile = os.path.split(os.path.realpath(__file__))[0] + '/' + '../config/aliyun.conf'
		config = configparser.ConfigParser()
		config.read(configfile)
		filetypes = config.get('cdn', 'filetypes')
		command = 'cd %s%s && git diff-tree -r --name-status --no-commit-id %s %s' % (self.dirname, self.site, version_old, version_new)
		ssh = common.ssh.SSHClient(self.host, command)
		return ssh.execute()
		
