#!/usr/bin/env python
import sync.git
import configparser
import common.hosts
import os
import aliyun.cdn.flush as CDNFlush

CONFIGFILE = os.path.split(os.path.realpath(__file__))[0] + '/' + 'config/site.conf'
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIGFILE)
SITE = CONFIG.get('site', 'site')
D = CONFIG.get('site_root_dirname', SITE)
DOMAIN = CONFIG.get('site_static', SITE)
INS = common.hosts.Hosts(SITE)
HOSTS = INS.get()

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
		

#def get_m_file():
#	configfile = os.path.split(os.path.realpath(__file__))[0] + '/' + 'config/aliyun.conf'
#	config = configparser.ConfigParser()
#	config.read(configfile)
#	filetypes = config.get('cdn', 'filetypes')
#	ins = sync.git.Git(HOSTS[0], D, SITE)
#	stdout, stderr = ins.get_diff_files()
#	files = []
#	for i in stdout:
#		if re.match('M.*?\.%s' % filetypes, i):
#			files.append(i[1:].strip())
#	return files	
	

#def flush_cdn():
#	config = configparser.ConfigParser()
#	config.read(CONFIGFILE)
#	domain = config.get('site_static', SITE)
#	args_dict = {}
#	args_dict['Action'] = 'RefreshObjectCaches'
#	args_dict['ObjectType'] = 'File'
#	ins = sync.git.Git(HOSTS[0], D, SITE)
#	files = ins.get_m_files()
#	if files:
#		for f in files:
#			args_dict['ObjectPath'] = DOMAIN + '/' + f
#			print('flush http://%s' % args_dict['ObjectPath'])
#			ins = format_url.Format(args_dict)
#			url = ins.compose_url()
#			res = req_flush_api(url)
#			print(res)
#			
#	else:
#		print('no file need to flush!')

#def req_flush_api(url):
#	try:
#		with urllib.request.urlopen(url) as res:
#			res = res.read()
#		res = res.decode('utf-8')
#		return res
#	except urllib.error.HTTPError as res:
#		return res


if __name__ == '__main__':
	release()
