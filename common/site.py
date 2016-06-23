#!/usr/bin/env python
#-- coding:utf-8 --
import common.mysql
import json


class Site(object):
	def __init__(self, domain):
		self.domain = domain
	
	def get_hosts(self):
		'''
		获取站点所在服务器IP列表
		'''
		cmd = '''select b.host from re_site a left join re_hosts b on a.id=b.did where domain=%s'''
		args = (self.domain,)
		con = common.mysql.Connect()
		res = json.loads(con.execute(cmd, args))
		hosts = []
		for h in res:
			hosts.append(h['host'])
		return hosts

	def get_site_info(self):
		'''
		获取站点信息,如站点静态域名、站点cdn状态、站点cdn服务商、站点程序所在目录的父目录
		'''
		cmd = '''select * from re_site where domain=%s'''
		args = (self.domain,)
		con = common.mysql.Connect()
		res = con.execute(cmd, args)
		return res
