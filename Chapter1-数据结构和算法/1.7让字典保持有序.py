#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 18:16
# @Author   :洪松
# @File     :1.7让字典保持有序.py

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print(d)
for key in d:
    print(key,d[key])

import json
print(json.dumps(d))
