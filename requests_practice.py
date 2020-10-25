# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:29:52 2020

@author: 阿欣
"""

import requests
import time
from tqdm import tqdm#进度条
for i in tqdm(range(1,101)):
    time_0=time.time()
    i=0
    while i<1000:
        def getHTMLText(url):
            try:
                r=requests.get('https://www.icourse163.org/learn/BIT-1001870001?tid=1450316449#/learn/content?type=detail&id=1214620494&cid=1218397643',timeout=30)
                r.raise_for_status()#如果状态不是200，引发HTPError异常
                r.encoding=r.apparent_encoding
                return r.text
            except:
                return "产生异常"
        i=i+1
        continue
time_1=time.time()  
total_time=time_1-time_0
print(total_time)