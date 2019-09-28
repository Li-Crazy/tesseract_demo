'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/25 22:09
@Software: PyCharm
@File    : demo1.py
'''
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\TesseractOCR\tesseract.exe"

image = Image.open(r'C:\Users\19845\Desktop\09.png')
text = pytesseract.image_to_string(image,lang='chi_sim')
print(text)