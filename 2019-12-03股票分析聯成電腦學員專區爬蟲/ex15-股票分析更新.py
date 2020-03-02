# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:30:16 2019

@author: user
"""

import requests
#import numpy as np
#import pandas as pd
import datetime
import time
import pymysql
m_host='localhost'
m_db='lcc'
m_user='root'
m_pwd='123456789'

def connect_mysql():
    global connect,cursor
    connect = pymysql.connect(host=m_host,db=m_db,user=m_user,password=m_pwd,charset='utf8',use_unicode=True)
    cursor = connect.cursor()

def get_stock_history(date,stock):
    #quotes=list()
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
    
    insertDB(data)
    
    return data

def insertDB(data):
    sql = "select * from stock where date='%s' and no='%s'" % (data[0],no)
    cursor.execute(sql)
    res=cursor.fetchone()
    if not res:
        insertsql = "insert into stock(date,no,amount,open,close,high,low) values('%s','%s','%d','%f','%f','%f','%f')" % (data[0],no,data[1],data[3],data[6],data[4],data[5])
        cursor.execute(insertsql)
        connect.commit()
        
def transform_date(date):
    y,m,d = date.split('/')
    return str(int(y)+1911)+'/'+m+'/'+d

def create_df(date,stock_no):
    global no
    no = stock_no
    get_stock_history(date,stock_no)
   

connect_mysql()

listStock=['2330']
for i in range(len(listStock)):
    result = create_df('20191128',listStock[i])
    
    
connect.close()