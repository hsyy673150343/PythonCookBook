#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/29 20:14
# @Author   : 洪松
# @File     : 2.16以固定的列数重新格式化文本.py

import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent=' '))
print(textwrap.fill(s, 40, subsequent_indent=' '))


