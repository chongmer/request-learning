# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:47:44 2020

@author: 阿欣
"""

import re
#re库默认使用贪婪匹配的方式，即输出匹配最长的字符串
m=re.search(r'PY.*N','PYaNcnNdieN')
print(m.group(0))

#最小匹配（输出最短的字符串）
n=re.search(r'PY.*?N','PYaNcnNdieN')
print(n.group(0))