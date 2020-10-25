# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:47:29 2020

@author: 阿欣
"""

#提取html中的所有url链接
import requests
from bs4 import BeautifulSoup
import re
import time

time_0=time.time()
url='https://www.w3.org/html/'
r=requests.get(url)
demo=r.text

soup=BeautifulSoup(demo,'html.parser')
#print(soup)


#for link in soup.find_all('a'):#find_all在soup的变量中查找信息
    #print(link.get('href'))
    
#print(soup.find_all('a'))
    
'''for tag in soup.find_all(True):
    print(tag.string)#打印所有标签名称用tag.name;打印标签属性tag.attrs,打印字符串tag.string'''


#只显示以m开头的标签（使用第三方库：正则表达式库）
'''for tag in soup.find_all(re.compile('m')):
    print(tag.name)'''
    
#输出标签html中包含org字符串的信息
'''for tag in soup.find_all('a','org'):#写错了。没有输出
    print(tag)'''

#print(soup.find_all(id='link1'))#输出空的值。
#因为没有精确定位，下面引入正则表达式来输出所有的id属性值
#print(soup.find_all(id=re.compile('content')))
'''print(soup.find_all('a'))
print('____________________')
print(soup.find_all('a',recursive=False))#recursive是否对子孙全部检索。
#默认值为ture(全部检索)。false则只对子标签进行检索'''

#检索字符串信息
#print(soup.find_all(string='Standards'))#（必须精确地输入字符串信息）
#下面用含有正则表达式的，全部检索
print(soup.find_all(string=re.compile('HTML')))

#tag.find_out()很常用，经常可以写为tag()
#同样，soup.find_out()可以写为soup()
print('______________')
print(soup(string=re.compile('HTML')))

time_1=time.time()
total_time=time_1-time_0
print(total_time)
