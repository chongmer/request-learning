# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 21:23:42 2020

@author: 阿欣
"""

from bs4 import BeautifulSoup

newsoup=BeautifulSoup("<b><!This is a comment.></b><p><This is not a comment.></p>","html.parser")#html中的注释
print(newsoup.b.string)
print(type(newsoup.b.string))
print(newsoup.p.string)
print(type(newsoup.p.string))