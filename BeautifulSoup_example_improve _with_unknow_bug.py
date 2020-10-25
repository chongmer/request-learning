# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:21:55 2020

@author: 阿欣
"""

import requests
from bs4 import BeautifulSoup
import bs4

#优化：解决中文字符对齐的问题

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''#返回一个空字符串
        
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:#需要过滤掉非标签类型的其他信息
        if isinstance(tr,bs4.element.Tag):#检测标签类型，如果标签类型不是bs4定义的tag类型，将过滤掉
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
    
def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10})"#{3}表示用第三种（中文)来填充.但是输出不了
    print(tplt.format("排名","学校名称","总分"),chr(12288))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2]),chr(12288))
#num参数表示希望将多少个元素打印出来

def main():
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
print(main())