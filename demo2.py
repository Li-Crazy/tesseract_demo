'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/26 12:59
@Software: PyCharm
@File    : demo2.py
'''
import pytesseract
from urllib import request
from PIL import Image
import time

def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\TesseractOCR\tesseract.exe"
    url = "https://passport.lagou.com/vcode/create?from=register&refresh=1513082201055"
    while True:
        request.urlretrieve(url,'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(3)
        break

if __name__ == '__main__':
    main()