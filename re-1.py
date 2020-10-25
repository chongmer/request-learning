# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:06:34 2020

@author: 阿欣
"""

import re

#match函数及match对象的使用方法
match=re.search(r'[1-9]\d{5}','BIT100081')

if match:
    print(match.group(0))
    print(match.start)
    print(match.end)
    print(match.span)
#regex=re.compile(r'[1-9]\d{5}')
#print(re.finditer(regex,'BIT100081 TSU100084'))
    

#print(type(match))
#print(match.endpos)
#print(match.group(0))
    
#findall函数（返回的是列表类型）
#ls=re.findall(r'[1-9]\d{5}','BIT 100081 TSU 100084')
    
#split函数分割，返回字符串
#ls=re.split(r'[1-9]\d{5}','BIT100081 TSU100084')
#ls=re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1)#最大分割数

#print(ls)
    
#finditer迭代处理
'''for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
    if m:
        print(m.group(0))'''

#sub替换所有匹配的字符串，返回替换后的字符串
#print(re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084'))

#compile能够将正则表达式的字符串形式编译成正则表达式对象 
#re.search()相当于regex=re.compile()加regex.search()
#regex=re.compile(r'[1-9]\d{5}')