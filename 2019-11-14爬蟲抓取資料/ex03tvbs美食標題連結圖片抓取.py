# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:10:24 2019

@author: user
"""

import requests
from bs4 import BeautifulSoup
url='https://supertaste.tvbs.com.tw/topic/22'
content=requests.get(url).text
soup=BeautifulSoup(content,'html.parser')

alldata = soup.find(id='combolistUl')

allcontent = alldata.find_all('li')

for row in allcontent:
    link = 'https://supertaste.tvbs.com.tw'+row.find('a').get('href')
    img = row.find('img').get('data-original')
    title = row.find(class_='txt').text 
    print('標題:',title)
    print('連結:',link)
    print('圖片:',img)
    print('-'*80)