# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 21:20:01 2019

@author: user
"""

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(Image.open('test.jpg')))