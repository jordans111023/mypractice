# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json

url='http://tbike.tainan.gov.tw:8081/Service/StationStatus/Json'
response=requests.get(url).text
data=json.loads(response)
for row in data:
    print('站名:',row['StationName'])
    print('可借:',row['AvaliableBikeCount'])
    print('可停:',row['AvaliableSpaceCount'])
    print('-'*50)