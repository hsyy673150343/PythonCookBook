#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/25 19:21
# @Author   : 洪松
# @File     : 1.16筛选序列中的元素.py

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])


pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

#------------------------------------------------#

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

#------------------------------------------------#


import math
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([math.sqrt(n) for n in mylist if n > 0])

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

#------------------------------------------------#
from itertools import compress

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
print(more5)

print(list(compress(addresses, more5)))
