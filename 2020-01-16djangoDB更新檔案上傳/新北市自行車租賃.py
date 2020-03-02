# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json

url='https://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json'
response=requests.get(url).text
data=json.loads(response)
for row in data:
    print('站名:',row['sna'])
    print('可借:',row['bemp'])
    print('可停:',row['sbi'])
    print('-'*50)