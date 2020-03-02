# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:55:35 2019

@author: user
"""

import requests
from bs4 import BeautifulSoup


header={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

content=requests.get("https://web.cpc.com.tw/division/mb/oil-more1-1.aspx",headers=header).text#抓網頁裡面的標頭

soup=BeautifulSoup(content,'html.parser')

data=soup.find(id='Showtd')

allrows = data.find_all('tr')

i=0

for row in allrows:
    i+=1
    if i>=1:
        cols=row.find_all('td')
        print(cols[1].text,cols[6].text,)
        print()