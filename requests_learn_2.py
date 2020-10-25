# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:49:00 2020

@author: 阿欣
"""
#爬取网页的通用代码框架

import requests
#requests库重点掌握head和get两个方法

R=requests.request('HEAD','https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6',timeout=10)
#timeout设置超时时间，以s为单位。
#proxies字典类型，设置访问代理服务器，可以增加登录认证。有效防止对于爬虫的逆追踪。
#data,headers,json字段需要灵活掌握。
print(R)
#网络连接有风险、处理异常很重要。
'''def getHTMLText(url):
    try:
        r=requests.get('https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6',timeout=30)
        r.raise_for_status()#如果状态不是200，引发HTPError异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
print(getHTMLText('https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6'))'''