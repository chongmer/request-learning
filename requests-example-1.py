# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:38:47 2020

@author: 阿欣
"""

import requests

'''url="https://top.jd.com/?cateId=1583&itemId=8052643"
try:
    r=requests.get(url)
    r.raise_for_status()#如果状态不是200，引发HTPError异常
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')'''

'''print('______________')
m=requests.get('https://www.amazon.cn/gp/product/B07FQKB4TM/ref=amb_link_2?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-leftnav&pf_rd_r=ECA0JGBYKZVSKDB13WJ6&pf_rd_r=ECA0JGBYKZVSKDB13WJ6&pf_rd_t=101&pf_rd_p=bffe5c57-abb7-4353-a435-574b62c2e33e&pf_rd_p=bffe5c57-abb7-4353-a435-574b62c2e33e&pf_rd_i=116087071')
print(m.status_code)#返回503
print(m.encoding)
m.encoding='utf-8'
print(m.status_code)#还是返回503，且'抱歉，我们只是想确认一下当前访问者并非自动程序。为了达到最佳效果，请确保您浏览器上的 Cookie 已启用'
print(m.request.headers)#'User-Agent': 'python-requests/2.22.0'爬虫访问被拒绝（来源审查）。
#print(m.text)'''

kv={'user-agent':'Mozilla/5.0'}
m=requests.get('https://www.amazon.cn/gp/product/B07FQKB4TM/ref=amb_link_2?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-leftnav&pf_rd_r=ECA0JGBYKZVSKDB13WJ6&pf_rd_r=ECA0JGBYKZVSKDB13WJ6&pf_rd_t=101&pf_rd_p=bffe5c57-abb7-4353-a435-574b62c2e33e&pf_rd_p=bffe5c57-abb7-4353-a435-574b62c2e33e&pf_rd_i=116087071',headers=kv)
print(m.status_code)
print(m.encoding)
m.encoding='utf-8'
print(m.request.headers)
print(m.text)
