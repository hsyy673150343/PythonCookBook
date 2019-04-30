#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 18:05
# @Author   :洪松
# @File     :1.6在字典中将键映射到多个值上.py

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

d = {}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)
print(d)