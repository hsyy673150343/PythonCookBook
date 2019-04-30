#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 20:04
# @Author   : 洪松
# @File     : 2.11从字符串中去掉不需要的字符.py


s1 = ' hello word \n'
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())

s2 = '-------------hello============='
print(s2.lstrip('-'))
print(s2.rstrip('='))
print(s2.strip('-='))
