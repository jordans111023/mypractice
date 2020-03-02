# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:37:39 2019

@author: user
"""

import requests

url='https://member.lccnet.com.tw/login.asp'

param={'NO':'100681338','PWD':'}

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

data = requests.post(url,headers=header,data=param)
data.encoding='utf8'

print(data.text)
