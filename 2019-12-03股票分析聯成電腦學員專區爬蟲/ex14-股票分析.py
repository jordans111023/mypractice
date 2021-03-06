# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:30:16 2019

@author: user
"""

import requests
import numpy as np
import pandas as pd
import datetime

def get_stock_history(date,stock):
    quotes=list()
    url='http://www.twse.com.tw/exchangeReport/STOCK_DAY?date=%s&stockNo=%s' %( date, stock)
    
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    
    r=requests.get(url,headers = header)
    data=r.json()
    return transform(data['data'])

def transform(data):
    return [transform_data(d) for d in data]

def transform_data(data):
    data[0]=datetime.datetime.strptime(transform_date(data[0]),'%Y/%m/%d')
    data[1]=int(data[1].replace(',',''))
    data[2]=int(data[2].replace(',',''))
    data[3]=float(data[3].replace(',',''))
    data[4]=float(data[4].replace(',',''))
    data[5]=float(data[5].replace(',',''))
    data[6]=float(data[6].replace(',',''))
    data[7]=float(0.0 if data[7].replace(',','')=='X0.00' else data[7].replace(',',''))
    data[8]=int(data[8].replace(',',''))
    
    return data

def transform_date(date):
    y,m,d = date.split('/')
    return str(int(y)+1911)+'/'+m+'/'+d

def create_df(date,stock_no):
    s=pd.DataFrame(get_stock_history(date,stock_no))
    s.columns = ['date','成交股數','成交金額','開盤價','最高價','最低價','收盤價','漲跌','筆數']
    stock = list()
    
    for d in range(len(s)):
        stock.append(stock_no)
    
    s['stockno'] = pd.Series(stock,index=s.index)
    datelist = list()
    
    for d in range(len(s)):
        datelist.append(s['date'][d])
    
    s.index = datelist
    s2 = s.drop(['date'],axis=1)
    mlist=list()
    
    for item in s2.index:
        mlist.append(item.month)
        
    s2['month']=mlist
    return s2

listStock=['2330']
for i in range(len(listStock)):
    result = create_df('20191128',listStock[i])
    print(result)