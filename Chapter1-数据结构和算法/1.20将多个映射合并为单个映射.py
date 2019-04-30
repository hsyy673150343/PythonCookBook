#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/25 20:51
# @Author   : 洪松
# @File     : 1.20将多个映射合并为单个映射.py


from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])


print(len(c))
print(list(c.keys()))
print(list(c.values()))
print(c)


c['z'] = 10
c['w'] = 40
print(c)
# del c['y']#KeyError: "Key not found in the first mapping: 'y'" 修改映射的操作总是会作用在列出的第一个映射结构上
del c['x']
print(c)
#------------------------------------------------------------#
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)

print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])

#----------------------------------------------------------------#
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)
print(merged['x'], merged['y'], merged['z'])

a['x'] = 13
print(merged['x'])#任何一个原始字典做了修改，这个改变都不会反应到合并后的字典中
print(a['x'])

#-----------------------------------------------------------------#
'''ChainMap使用的就是原始字典'''
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 99
print(merged['x'])
