# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:57:24 2020

@author: 阿欣
"""
#淘宝商品比价定向爬虫(获取页面中的商品信息，提取名称和价格)
#淘宝的搜索接口
#翻页的处理

import requests
import re

url='https://s.taobao.com/search?q=书包'
m=requests.get('https://s.taobao.com/robots.txt')
print(m.text)
#子函数
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return''

def pasaePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"\[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?"',html)#最小匹配
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(plt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print('')
            
def PrintGoodList(ilt):
    tplt="{:4}\t{:8}\t{:16}"#输出的格式
    print(tplt.format('序号','价格','商品名称'))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))

#主函数
def main():
    goods='书包'
   #depth=2#爬取当前页和下一页
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]#输出结果
    for i in (0,3):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            pasaePage(infoList,html)
        except:
            continue
    print(PrintGoodList(infoList))

print(main())
            

