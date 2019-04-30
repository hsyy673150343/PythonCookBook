#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 19:26
# @Author   : 洪松
# @File     : 2.9将Unicode文本统一表示为规范性形式.py
import unicodedata
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)
print(s1 == s2)
print(len(s1))
print(len(s2))


t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))

t1 = unicodedata.normalize('NFD', s1)
print(t1)
x = ''.join(c for c in t1 if not unicodedata.combining(c))
print(x)
