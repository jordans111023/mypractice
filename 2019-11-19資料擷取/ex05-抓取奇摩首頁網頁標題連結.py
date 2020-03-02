# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:44:30 2019

@author: user
"""

import requests
from bs4 import BeautifulSoup

url='https://tw.yahoo.com/'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

content=requests.get(url,headers=header).text#抓網頁裡面的標頭

soup=BeautifulSoup(content,'html.parser')

storys=soup.find_all('a',class_='story-title')

for s in storys:
    print('標題:',s.text)
    print('連結:',s.get('href'))
    print('-'*50)