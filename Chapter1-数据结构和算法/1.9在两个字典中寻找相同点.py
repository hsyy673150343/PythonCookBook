#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 21:18
# @Author   :洪松
# @File     :1.9在两个字典中寻找相同点.py

a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}
#找到相同的键
print(a.keys() & b.keys())
#找到在a中而不在b中的键
print(a.keys() - b.keys())
#找到相同的键值对
print(a.items() & b.items())

c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)