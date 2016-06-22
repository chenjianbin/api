#!/usr/bin/env python
import sync.git
import configparser
import common.hosts
import os
import aliyun.cdn.flush as CDNFlush

CONFIGFILE = os.path.split(os.path.realpath(__file__))[0] + '/' + 'config/site.ini'
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIGFILE)
SITE = CONFIG.get('site', 'site')
D = CONFIG.get('site_root_dirname', SITE)
DOMAIN = CONFIG.get('site_static', SITE)
INS = common.hosts.Hosts(SITE)
HOSTS = INS.get()

#class Release(object):
#	def __init__(self, domain):
#		self.domain = domain
def release():
	for h in HOSTS:
		ins = sync.git.Git(h, D, SITE)
		stdout, stderr = ins.pull()
		git_pull_message = '%s  git pull on host %s  %s' % ('#'*20, h, '#'*20)
		print(git_pull_message)
		for so in stdout:
			print(so, end='')
		for se in stderr:
			print(se, end='')
		print('%s' % '#'*len(git_pull_message), end='\n\n\n')
	flush_cdn_message = '%s  flush cdn  %s' % ('#'*20, '#'*20)
	print(flush_cdn_message)
	ins1 = sync.git.Git(HOSTS[0], D, SITE)
	files = ins1.get_m_files()
	if files:
		ins2 = CDNFlush.Flush(DOMAIN, files)
		ins2.run()
	else:
		print('no file need to flush!')
	print('%s' % '#'*len(flush_cdn_message))
		


if __name__ == '__main__':
	release()
