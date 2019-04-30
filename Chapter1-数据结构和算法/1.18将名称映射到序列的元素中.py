#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/25 20:11
# @Author   : 洪松
# @File     : 1.18将名称映射到序列的元素中.py
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('19080166480@163.com', '2019-04-25')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))

address, jion = sub
print(address)
print(jion)

#---------------------------------------------------------------#
Stock = namedtuple('Stock',['name', 'shares', 'price'])
s = Stock('NIKE', 100, 123.45)
print(s)
# s.shares = 75# 报错：AttributeError: can't set attribute 因为namedtuple是不可变的

s = s._replace(shares=75)
print(s)

#-----------------------------------------------------------------------------------#

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)#创建一个包含默认值的"原型"元组

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name':'Bob', 'shares':100, 'price':123.45}
print(dict_to_stock(a))