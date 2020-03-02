# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:11:25 2019

@author: user
"""

import requests
from bs4 import BeautifulSoup
url='https://news.tvbs.com.tw/local'
content=requests.get(url).text
soup=BeautifulSoup(content,'html.parser')

allh2=soup.find_all('h2')
for row in allh2:
    print(row.text)#只抓h2裡面的文字

