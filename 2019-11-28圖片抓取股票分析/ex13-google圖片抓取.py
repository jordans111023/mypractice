# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import urllib.request

url='https://www.google.com.tw/search?q=%E9%AD%AF%E5%A4%AB&source=lnms&tbm=isch&sa=X&ved=2ahUKEwia44it3ozmAhVfyosBHStlCBcQ_AUoAXoECA8QAw&biw=1034&bih=645'

data = requests.get(url).text

#print (data)

soup=BeautifulSoup(data,'html.parser')

content = soup.find('div',{'id':'ires'})

alldata = content.find_all('a')

#print(alldata)

i=1
for row in alldata:
    url = row.img['src']
    urllib.request.urlretrieve(url,str(i)+'.jpg')
    i=i+1
    
