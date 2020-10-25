# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:05:20 2020

@author: 阿欣
"""

#生成器yield写法，节省空间，效率更高 
m=[]
def gen(n):
    for i in range(n):
        yield i**2

for i in gen(5):
    m.append(i)
print(m)