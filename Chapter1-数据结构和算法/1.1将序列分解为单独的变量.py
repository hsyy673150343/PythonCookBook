#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 23:41
# @Author   :洪松
# @File     :1.1将序列分解为单独的变量.py


#只要对象是可迭代的(字符串，文件，迭代器，生成器)，那么就可以执行分解操作#

p = (4,5)
x,y = p
print(x)
print(y)

data = ['hongsong', 40, 50.1, (2012, 12, 31)]
name, shares, price, date = data
print(name,shares,price,date)
name, shares, price, (year, month, day) = data
print(name, shares, price, (year, month, day))


s = 'Hello'
a,b,c,d,e = s
print(a,b,c,d,e)


data = ['hongsong', 40, 50.1, (2012, 12, 31)]
_, shares, _, data = data
print(shares)
print(data)