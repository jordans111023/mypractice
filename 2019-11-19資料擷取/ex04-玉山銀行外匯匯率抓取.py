# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup


header={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

content=requests.get("https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates",headers=header).text#抓網頁裡面的標頭

soup=BeautifulSoup(content,'html.parser')

data=soup.find(id='inteTable1')

allrows = data.find_all('tr')

print('外幣   ','即期買入','即期賣出')

i=0

for row in allrows:
    i+=1
    if i>=3:
        cols=row.find_all('td')
        print(cols[0].text,cols[1].text,cols[2].text,cols[3].text,cols[4].text,cols[5].text,cols[6].text)
        print()
        