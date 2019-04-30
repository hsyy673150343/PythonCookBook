#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/29 19:07
# @Author   : 洪松
# @File     : 2.14字符串连接及合并.py


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago'


text = ''.join(sample())
print(text)


import sys

for part in sample():
    sys.stdout.write(part)
sys.stdout.write('\n')

# (c) Combination of parts into buffers and larger I/O operations


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


for part in combine(sample(), 32768):
    sys.stdout.write(part)
sys.stdout.write('\n')