# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:51:35 2019

@author: user
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import selenium


driverpath='C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driverpath)
driver.implicitly_wait(3)#啟動後過三秒後開始抓

driver.get('https://supertaste.tvbs.com.tw/topic/22')
for i in range(10):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    
soup=BeautifulSoup(driver.page_source,'html.parser')
data=soup.find(id='combolistUl')
print(data)