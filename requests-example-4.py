# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:20:19 2020

@author: 阿欣
"""

import requests

path="D:/abc.jpg"
url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1595689843726&di=d1c3f50caa56743b2aea806a99f42c83&imgtype=0&src=http%3A%2F%2Fpic.rmb.bdstatic.com%2Ff9b39493c1730a879629a21df44794a5.jpeg'
r=requests.get(url)
print(r.status_code)

#下面保存图片（二进制文件）
with open(path,'wb') as f:
    f.write(r.content)
print(f)
f.close()