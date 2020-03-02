# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:45:48 2019

@author: user
"""

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
        if tag=='Stop':
            self.car=attributes['nameZh']
            self.time=attributes['latitude']
            print(self.car)
            print(self.time)
            print('-'*50)


if (__name__=='__main__'):
    parser=xml.sax.make_parser() #建立一個解析器
    handler=XMLHandler() 
    parser.setContentHandler(handler)#讓解析器去處理
    url='http://ibus.tbkc.gov.tw/xmlbus/StaticData/GetStop.xml?routeIds=100'
    result=requests.get(url).text
    new_file='bus.xml'
    new_xml=open(new_file,'w',encoding='UTF-8')
    new_xml.write(result)
    new_xml.close()
    parser.parse(new_file)
    
