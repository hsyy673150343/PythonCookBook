#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/29 20:41
# @Author   : 洪松
# @File     : 2.20在字节串上执行文本操作.py

data = b'Hello word'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'word', b'hsyy'))


data_array = bytearray(b'Hello Word')
print(data_array[0:5])
print(data_array.startswith(b'Hello'))
print(data_array.split())
# print(data_array.replace(b'word', b' word hs_yy'))#没有替换成功

# -------------------------------------#

data = b'FOO:BAR, SPAM'
import re
# print(re.split('[:,]', data))#TypeError: cannot use a string pattern on a bytes-like object
print(re.split(b'[:,]', data))


# ----------------------------------------------#
a = 'Hello World'
print(a[0])

b = b'Hello world'
print(b[0])
print(b)

b_string = b.decode('ascii')
print(b_string)

# ----------------------------------------------------#
b_string_format = '{:10s} {:10d} {:10.2f}'.format('Hongsong', 100, 490.1).encode('ascii')
print(b_string_format)