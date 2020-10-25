# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:18:06 2020

@author: 阿欣
"""

import scrapy

def startRequest(self):
    urls=[
      'https://so.csdn.net/so/search/s.do?q=python%20%E6%95%B0%E7%BB%84%E6%B7%BB%E5%8A%A0%E5%85%83%E7%B4%A0&t=&u=',
      'https://blog.csdn.net/aaqq3561/article/details/48244997?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522159711079919724846458360%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=159711079919724846458360&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v3~pc_rank_v2-1-48244997.first_rank_ecpm_v3_pc_rank_v2&utm_term=python+%E6%95%B0%E7%BB%84%E6%B7%BB%E5%8A%A0%E5%85%83%E7%B4%A0&spm=1018.2118.3001.4187'
      ]
    for url in urls:
        yield scrapy.Request(url,callback=self.parse)
def parse(self,response):
    fname=response.url.split('/')[-1]
    with open (fname,'wb') as f:
        f.write(response.body)
    self.log('Saved file %s.' % fname)
        