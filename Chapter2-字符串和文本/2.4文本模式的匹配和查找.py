#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/27 21:42
# @Author   : 洪松
# @File     : 2.4文本模式的匹配和查找.py
import re
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')


if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')


#---------------------------------------------------#
datepat = re.compile(r'\d+/\d+/\d+')#将正则表达式模式预编译成一个模式对象

if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

#---------------------------------------------------#
text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
res = datepat.findall(text)
print(res)

#---------------------------------------------------#
m = datepat.match('11/27/2012')
print(m)
# print(m.group(0))


print(datepat.findall(text))


for m in datepat.finditer(text):
    print(m.group(0))