#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/27 22:17
# @Author   : 洪松
# @File     : 2.5查找和替换文本.py

import re
text = 'yy, yy, yy, hs, yy, hs'
print(text.replace('yy','hs'))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n, sep='\n')