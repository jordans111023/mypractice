# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

soup.find只找一個檔案出來

soup.find_all 找出裡面所有檔案
"""

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

soup=BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())

data=soup.find_all(['a','b'],limit=2)#限制最多2筆超過就不會出現
print('多標籤:',data)

aid=soup.find(id='link2')
print('aid:',aid)

h2txt=soup.find('h2').text
alldata=soup.find_all('a')
for row in alldata:
    txt=row.text
    link=row.get('href')
    print('文字:',txt)
    print('連結:',link)
    