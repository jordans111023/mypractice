# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 19:58:37 2019

@author: user
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs

url = 'https://member.lccnet.com.tw/login.asp'
NO='100681338'
PWD=''

driverpath = 'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driverpath)
driver.maximize_window()
driver.get(url)

driver.find_element_by_id('NO').send_keys(NO)#自動輸入帳號
driver.find_element_by_id('PWD').send_keys(PWD)#自動輸入密碼
driver.find_element_by_css_selector('button').click()#自動按登入按鈕

driver.get('https://member.lccnet.com.tw/myclass_index.asp')  #自動抓取我的課程資料
soup = bs(driver.page_source,'html.parser')
print(soup)
