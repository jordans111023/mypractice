# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

from bs4 import BeautifulSoup

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='123456789',database='lcc',charset='utf8')
cursor = conn.cursor() 

url = 'https://tw.buy.yahoo.com/category/4385994'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

key = input('請輸入NB品牌:')

param = {'flt':'品牌_'+key}

content = requests.get(url,headers = header, params = param).text

soup = BeautifulSoup(content,'html.parser')

nb = soup.find_all('li',class_='BaseGridItem__grid___2wuJ7 imprsn BaseGridItem__multipleImage___37M7b') 

#print(nb[0]) 

for row in nb:
    link = row.find('a').get('href')
    img = row.find('img').get('srcset')
    firstimg = img.split(',')
    nbimg = firstimg[0].split()
    values = list(row.stripped_strings)#只剩下裡面的字串
    price = values[1].replace('$','')#去除$
    price = price.replace(',','')#去除,變成整數以後可以價格比較
    if values[0] !='補貨中':#老師經驗談  把補貨中的商品拿掉 才不會出錯
        sql = "select * from products where webname='Yahoo' and title='{}'".format(values[0])
        cursor.execute(sql)
        if cursor.rowcount == 0:
            sql="insert into products (webname,title,price,link,photo) values('Yahoo','{}',{},'{}','{}')".format(values[0],price,link,nbimg[0])
            cursor.execute(sql)
            conn.commit()
        print('產品:',values[0])
        print('價格:',price)
        print('連結:',link)
        print('圖片:',nbimg[0])
        print()
cursor.close()
conn.close() 
    