#!/usr/bin/env python
#-- coding:utf-8 --
import urllib.request
import urllib.error
import format_url



args_dict = {'Action':'RefreshObjectCaches', 'ObjectPath':'static.zhangshangduobao.net/statics/templates/templet4/css/style.guide.css', 'ObjectType':'File'}
url = format_url.FormatURL(args_dict).compose_url()
print(url)
try:
	with urllib.request.urlopen(url) as res:
		res = res.read()
		res = res.decode('utf-8')
		print(res)
except urllib.error.HTTPError as res:
		print(res)
	
