# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:25:30 2019

@author: user
"""

import requests
import json

url='https://data.ntpc.gov.tw/od/data/api/28AB4122-60E1-4065-98E5-ABCCB69AACA6?$format=json'
response=requests.get(url).text
data=json.loads(response)
for row in data:
    print('車牌:',row['car'])
    print('位置:',row['location'])
    
    print('-'*50)