# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
#from bs4 import BeautifulSoup

url = 'http://www.thsrc.com.tw/tw/TimeTable/Search'
data={'StartStationName':  '台中站',
'EndStationName':  '台北站',
'SearchType': 'S',
'StartStation': '3301e395-46b8-47aa-aa37-139e15708779',
'EndStation': '977abb69-413a-4ccf-a109-0272c24fd490',
'DepartueSearchDate': '2019/12/06',
'DepartueSearchTime': '06:00'}

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
response = requests.post(url,headers=header,data=data).text

#print(response)

import json
data = json.loads(response)
trainItem = data['data']['DepartureTable']['TrainItem']
trainNumber = list()
departureTime = list()
destinationTime = list()
duration = list()
for item in trainItem:
    trainNumber.append(item['TrainNumber'])
    departureTime.append(item['DepartureTime'])
    destinationTime.append(item['DestinationTime'])
    duration.append(item['Duration'])
print(trainNumber[0],departureTime[0],destinationTime[0],duration[0])

import pandas as pd
highway = pd.DataFrame({'車次':trainNumber,'出發時間':departureTime,'到達時間':destinationTime,'行車時間':duration},columns=['車次','出發時間','到達時間','行車時間'])
print(highway)    