# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:38:57 2020

@author: 阿欣
"""

from bs4 import BeautifulSoup
import requests

#HTML页面是以尖括号为主的页面封装的信息
r=requests.get('https://developer.mozilla.org/zh-CN/docs/Web/HTML')
#print(r.text)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print('____________')
print(soup.title)

tag=soup.a
print(tag)
print(tag.string)
'''print(tag.attrs)#输出标签属性
print(tag.attrs['id'])#输出a标签的id属性
print(tag.attrs['href'])#输出a标签的链接属性
print(type(tag.attrs))#标签属性的类型
print(type(tag))
print(soup.a.name)'''
print(soup.a.parent.name)#包含a标签的上一层标签（父标签）的名字
print(soup.li)
print(soup.li.string)
print(type(soup.li.string))#NavigableString是可以跨越多个标签层次的
#print(soup.li.parent.name)
#print(soup.a.parent.parent.name)