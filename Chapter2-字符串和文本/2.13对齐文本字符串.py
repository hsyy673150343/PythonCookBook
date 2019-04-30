#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 20:21
# @Author   : 洪松
# @File     : 2.13对齐文本字符串.py

text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(text.ljust(20, '*'))
print(text.rjust(20, '*'))
print(text.center(20, '-'))

r = format(text, '>20')
le = format(text, '<20')
c = format(text, '^20')
print(r)
print(le)
print(c)


r1 = format(text, '=>20s')
print(r1)
c2 = format(text, '=^20s')
print(c2)


n = 1.34569
print(format(n, '>10'))
print(format(n, '>10.3f'))
