# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:55:23 2020

@author: 阿欣
"""

import requests

r=requests.get('https://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/')
print(r.status_code) #http请求的连接状态，200表示访问成功，404表示访问失败
#print(r.text)#http响应内容的字符串形式
#print(r.encoding)#根据HTTP header猜测出的响应内容编码方式。
#如果header存在charset字段则表明对其编码方式有要求。
#若无charset字段则认为编码为ISO-8859-1（不能解析中文）
#print(r.apparent_encoding)#根据内容分析出的响应内容编码方式
#r.encoding='utf-8'
#print(r.text)
print('_____________________')
#print(r.content)#HTTP响应内容的二进制形式
#print(type(r))
#print(r.headers)
