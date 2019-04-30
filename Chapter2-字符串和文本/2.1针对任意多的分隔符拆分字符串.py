#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/27 21:16
# @Author   : 洪松
# @File     : 2.1针对任意多的分隔符拆分字符串.py

import re
line = 'asdf fjdk; afed, fjek,asfd,   foo'
res_1 = re.split(r'[;,\s]\s*', line)
print(res_1)

res_2 = re.split(r'(;|,|\s)\s*', line)
print(res_2)

values = res_2[::2]
print(values)

#非捕获组 (?:....)
res_3 = re.split(r'(?:;|,|\s)\s*', line)
print(res_3)
