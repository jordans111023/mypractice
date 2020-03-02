# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:24:21 2019

@author: user
"""

import requests
from bs4 import BeautifulSoup


header={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

content=requests.get("https://supertaste.tvbs.com.tw/topic/22",headers=header).text#抓網頁裡面的標頭

soup=BeautifulSoup(content,'html.parser')

data =soup.select('.lazyimage')#   .是尋找class裡面的圖片
print(data)
print()