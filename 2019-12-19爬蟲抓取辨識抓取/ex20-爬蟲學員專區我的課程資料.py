# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup as bs

session_request = requests.session()
url ='https://member.lccnet.com.tw/login.asp'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
          'Cookie': '_gcl_au=1.1.1156711405.1576752848; _fbp=fb.2.1576752847970.776904128; _ga=GA1.3.1182939375.1576752848; _gid=GA1.3.1497800277.1576752848; _hjid=27f79c5a-252a-429e-8f3c-49e4c8f9bd5e; ASPSESSIONIDSUADTSAS=EKFJIMEBKMNPOLIKEDKLBODO; _ga=GA1.4.1182939375.1576752848; _gid=GA1.4.1497800277.1576752848; ASP.NET_SessionId=krrljmeosxov0sobkhi1pbb4; _dc_gtm_UA-8399363-4=1'}

userdata = {'NO':'100681338','PWD':''}
result = session_request.post(url,data=userdata,headers=header)
#送出資料 用post   抓取用get
classurl = 'https://member.lccnet.com.tw/myclass_index.asp'
myclass = session_request.get(classurl,headers=header)
myclass.encoding = 'big5'    
soup = bs(myclass.text,'html.parser')
#print(soup)  先看看有沒有資料跑出
allclass = soup.find(id='table85')
allrows = allclass.find_all('tr')
for row in allrows:
    td = row.find_all('td')
    print(td[0].text.strip(),
          td[1].text.strip(),
          td[2].text.strip(),
          td[3].text.strip(),
          td[4].text.strip())    #前後空白刪除
    

