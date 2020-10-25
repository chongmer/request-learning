# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:13:06 2020

@author: 阿欣
"""

import requests

kv={'wd':'python'}
r=requests.get('https://www.baidu.com/s',params=kv)#
print(r.status_code)
print(r.request.url)#发给百度的request的url是什么
print(len(r.text))