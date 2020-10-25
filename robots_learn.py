# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:26:47 2020

@author: 阿欣
"""

import requests

r=requests.get('http://www.qq.com/robots.txt')
print(r.text)

m=requests.get('http://news.qq.com/robots.txt')
print(m.text)
print('_______________')

n=requests.get('http://www.baidu.com/robots.txt')
print(n.text)
print('~~~~~~~~~~~~~~~~~~~')

o=requests.get('http://www.moe.edu.cn/robots.txt')
print(o.text)


#如果一个网站没有robots协议，代表这个网站允许任何爬虫无限制地爬取其内容