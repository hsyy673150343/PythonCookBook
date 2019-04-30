#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/25 15:58
# @Author   : 洪松
# @File     : 1.13通过公共键对字典列表排序.py

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

rows_by_uid_fname = sorted(rows, key=itemgetter('uid', 'fname'))
print(rows_by_uid_fname)

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(rows_by_fname)
print(rows_by_lfname)


rows_by_min = min(rows, key=itemgetter('uid'))
print(rows_by_min)
rows_by_max = max(rows, key=itemgetter('uid'))
print(rows_by_max)