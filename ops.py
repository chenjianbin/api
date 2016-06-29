#!/usr/bin/env python
import common.git
import common.site
import aliyun.cdn.flush as CDNFlush
import json

SITE = 'www.zhangshangduobao.net'
INS = common.site.Site(SITE)
HOSTS = INS.get_hosts()
INFO = json.loads(INS.get_site_info())[0]
DIR = INFO['dirname']
DOMAIN = INFO['flush_domain']

print(INFO)


#class Release(object):
#	def __init__(self, domain):
#		self.domain = domain
def release():
	for h in HOSTS:
		ins = sync.git.Git(h, DIR, SITE)
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
	ins1 = sync.git.Git(HOSTS[0], DIR, SITE)
	files = ins1.get_m_files()
	if files:
		ins2 = CDNFlush.Flush(DOMAIN, files)
		ins2.run()
	else:
		print('no file need to flush!')
	print('%s' % '#'*len(flush_cdn_message))
		


if __name__ == '__main__':
	release()
