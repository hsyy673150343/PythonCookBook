#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/25 20:39
# @Author   : 洪松
# @File     : 1.19同时对数据做转换和换算.py
import os

files = os.listdir('C:/Users/hongsongyangyang/PycharmProjects/PythonCookBook/Chapter1-数据结构和算法')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python')