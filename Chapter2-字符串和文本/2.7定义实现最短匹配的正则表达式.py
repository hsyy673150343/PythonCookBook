#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 17:53
# @Author   : 洪松
# @File     : 2.7定义实现最短匹配的正则表达式.py

import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
res1 = str_pat.findall(text1)
print(res1)


text2 = 'Computer says "no." Phone says "yes."'
res2 = str_pat.findall(text2)
print(res2)


str_pat1 = re.compile(r'\"(.*?)\"')
res3 = str_pat1.findall(text2)
print(res3)