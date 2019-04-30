#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/27 21:30
# @Author   : 洪松
# @File     : 2.2在字符串的开头或结尾处做文本匹配.py

import os
filename = os.listdir('.')
print(filename)

file = [name for name in filename if name.endswith('.py')]
print(file)

choices = ['http', 'ftp']
url = 'http://www.python.org'
# print(url.startswith(choices))#TypeError: startswith first arg must be str or a tuple of str, not list
print(url.startswith(tuple(choices)))