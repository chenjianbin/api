#!/usr/bin/env python
import common.mysql
import common.git
import common.svn
import common.site
import aliyun.cdn.flush as CDNFlush
import json

class Update(object):
	def __init__(self, domain):
		self.domain = domain

	def judge_domain(self):
		ins = common.site.Site(self.domain)
		info = json.loads(ins.get_site_info())
		if info:
			self.dirname = info[0]['dirname']
			self.version_control = info[0]['version_control']
			self.cdn_domain = info[0]['cdn_domain']
			self.cdn_status = info[0]['cdn_status']
			self.cdn_service = info[0]['cdn_service']
			self.hosts = ins.get_hosts()
		else:
			return 'The domain isn\'t registry !'

	def release_code(self):
		res = ''
		if self.version_control == 'git':
			for h in self.hosts:
				ins = common.git.Git(h, self.dirname, self.domain)
				stdout, stderr = ins.pull()
				message = '<p>%s  %s  %s</p>' % ('#'*20, h, '#'*20)
				for so in stdout:
					message = message + '<p>' + so + '</p>'
				for se in stderr:
					message = message + '<p>' + se + '</p>'
				res = res + message 
		elif self.version_control == 'svn':
			for h in self.hosts:
				ins = common.svn.Svn(h, self.dirname, self.domain)
				stdout, stderr = ins.update()
				message = '<p>%s  %s  %s</p>' % ('#'*20, h, '#'*20)
				for so in stdout:
					message = message + '<p>' + so + '</p>'
				for se in stderr:
					message = message + '<p>' + se + '</p>'
				res = res + message 
		else:
			res = '<p>The site not in version control</p>'
		return res

	def flush_cdn(self):
		message = '<p>%s  cdn  %s\n</p>' % ('#'*20, '#'*20)
		if self.cdn_status and self.cdn_domain and self.cdn_service:
			if self.version_control == 'git':
				ins = common.git.Git(self.hosts[0], self.dirname, self.domain)
			else:
				ins = common.svn.Sit(self.hosts[0], self.dirname, self.domain)
			files = ins.get_m_files()
			if files:
				flu = CDNFlush.Flush(self.cdn_domain, files)
				res = flu.run()
				message = message + res
			else:
				message = message + '<p>Nothing need to flush!\n</p>'
		else:
			message = message + '<p>The site doesn\'t have cdn cache</p>'
		return message
		
	def run(self):
		err_message = self.judge_domain()
		if err_message:
			return err_message
		else:
			message = self.release_code() + self.flush_cdn()
			return message	
		
