#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 22:29
# @Author   :洪松
# @File     :1.11对切片命名.py

record = '1kfjajfjoj33333333333330o03k00908997777979786669799987'
SHARES = slice(14,17)
PRICE = slice(30,33)
cost = int(record[SHARES]) * int(record[PRICE])
print(cost)


items = [0,1,2,3,4,5,6]
a = slice(2,4)
print(items[a])
items[a] = [10,11]
print(items)
del items[a]
print(items)

print(a.start)
print(a.stop)
print(a.step)


s = 'HelloWord'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])