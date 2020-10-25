# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:20:37 2020

@author: 阿欣
"""

#中国大学排名定向提取
#step1.获取大学排名的网络内容
#step2.提取网页内容到合适的数据结构
#step3. 利用数据结构展示并输出结果

import requests
from bs4 import BeautifulSoup
import bs4


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
    print("{:^10}\t{:^6}\t{:^10})".format("排名","学校名称","总分"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10})".format(u[0],u[1],u[2]))
#num参数表示希望将多少个元素打印出来

def main():
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
print(main())