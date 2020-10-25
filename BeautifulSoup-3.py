# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:40:55 2020

@author: 阿欣
"""
#遍历所有标签
import requests
from bs4 import BeautifulSoup
import time

time_0=time.time()
kv={'user-agent':'Mozilla/5.0'}
r=requests.get('https://www.w3.org/html/',headers=kv)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
#print(soup.head)
print(soup.head.name)

#下行遍历
'''print('_________________')
print(soup.head.contents)#head标签的子标签(及其字符串)
print('body子标签：',soup.body.contents)
print(len(soup.body.contents))#body标签下的元素个数
print(soup.body.contents[1])#获取第一个元素'''
#。contents返回的是列表类型。而.children和.descendants返回的类型只能用于for循环语句

#上行遍历
'''print('上行遍历')
print(soup.head.parent)
print('~~~~')
print(soup.head.parents)
print(soup.head.parent==soup.head.parents)
print(soup.html.parent)#html是最高级标签，所以其父标签只有它自己
print(soup.parent)'''

#平行遍历（同一个父节点下）
'''print(len(soup.body.contents))
#print(soup.body.contents[1])#获取第n个元素
print(soup.header.next_sibling)#a标签的下一个标签；可能不是标签而是得到了字符串
print('_______________')
#print(soup.header.next_sibling.next_sibling)
#print(soup.header.previous_sibling)'''

#prettify方法
'''print(soup.prettify)
print('_______________')
print(soup.header.prettify)'''
time_1=time.time()
total_time=time_1-time_0
print(total_time)