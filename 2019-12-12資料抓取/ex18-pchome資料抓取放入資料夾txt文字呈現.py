# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup


header={'User-Agent':'Googlebot',
        'Content-Type':'text/html;charset=utf-8'}

url='https://24h.pchome.com.tw/region/DHAA'

res=requests.get(url,headers=header,
                 allow_redirects=True)#.text
#print(res)

alldata = res.text.encode(res.encoding).decode('utf-8')
#print(alldata)

with open('pchome.txt','w',encoding='UTF-8')as fp:fp.write(alldata)
#直接把資料抓下來,放在資料夾裡面呈現txt文字檔,用w會將資料洗掉再將資料寫入,若不想洗掉可以用a

soup = BeautifulSoup(alldata,'html.parser',
                     from_encoding='utf8')

contents = soup.find_all('dd')
for row in contents:
    a = row.find_all('a')
    if len(a) > 2:
        price = row.find('span',class_='value')
        #print(a)
        #print(price)
        print(a[1].text)
        print(a[1].get('href'))
        print('-'*30)