#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 21:33
# @Author   :洪松
# @File     :1.10从序列中移除重复项且保持元素间顺序不变.py

#-------如果序列中的值是可希哈的(整数，浮点数，字符串，元组)---------#
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,2,1,9,1,5,10]
print(list(dedupe(a)))

#-------如果序列中的值是不可希哈的(列表)---------#
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))