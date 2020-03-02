# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:54:59 2019

@author: user
"""

import requests
from bs4 import BeautifulSoup

param = {'keyword':'哥吉拉'}

header = {'user-agent': 'Googlebot'
          ,'authority':'shopee.tw'}#Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36改為googlebot讓Google機器人來抓取可以爬生排位

url = 'https://shopee.tw/search'

data = requests.get(url,params=param,headers=header).text

soup=BeautifulSoup(data,'html.parser')

items=soup.find_all('div',class_='col-xs-2-4 shopee-search-item-result__item')

for row in items:
    link = row.find('a').get('href')
    title = row.find('div',class_='_1NoI8_ _2gr36I').text
    prices = row.find_all('span',class_='_341bF0')
    print('連結:','https://shopee.tw'+link)
    print('標題:','title')
    if len(prices) == 2:
        firstprice = prices[0].text.replace(',','')
        secondprice = prices[1].text.replace(',','')
        print('價格:',firstprice,'~',secondprice)
    else:
        firstprice = prices[0].text.replace(',','')
        print('價格:',firstprice)