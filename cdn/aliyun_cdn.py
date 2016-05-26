#!/usr/bin/env python
#-- coding:utf-8 --
''' manage aliyun cdn '''

import urllib.request
import 

url='http://'
aliyun_url='http://'

def flush():
    with urllib.request.openurl() as f:
        print (f.read())
