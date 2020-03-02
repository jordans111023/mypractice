# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:50:42 2019

@author: user
"""

import requests
import xml.sax #xml解析套件

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):#定義三個變數
        self.car=''
        self.time=''
        self.location=''
    
    def startElement(self,tag,attributes):
        self.startTag=tag
    
    def characters(self,content):
        if self.startTag=='car':
            self.car=content
        if self.startTag=='time':
            self.time=content
        if self.startTag=='location':
            self.location=content
    
    def endElement(self,tag):
        if self.startTag=='car':
            print('車號:',self.car)
        elif self.startTag=='time':
            print('時間:',self.time)
        elif self.startTag=='location':
            print('位置:',self.location)
        self.startTag=''

if (__name__=='__main__'):
    parser=xml.sax.make_parser() #建立一個解析器
    handler=XMLHandler() 
    parser.setContentHandler(handler)#讓解析器去處理
    url='https://data.ntpc.gov.tw/od/data/api/28AB4122-60E1-4065-98E5-ABCCB69AACA6?$format=xml'
    result=requests.get(url).text
    new_file='garbare.xml'
    new_xml=open(new_file,'w',encoding='UTF-8')
    new_xml.write(result)
    new_xml.close()
    parser.parse(new_file)
    
