#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/29 19:52
# @Author   : 洪松
# @File     : 2.15给字符串中的变量名做插值处理.py

s = '{name} has {n} messages.'
x = s.format(name='hs', n=24)
print(x)


name = 'yy'
n = 21
y = s.format_map(vars())
print(y)


# ------------------------------------- #
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('HS',30)
z = s.format_map(vars(a))
print(z)


# ----------------------------------------- #
# w = s.format(name='YY')
# print(w)#KeyError: 'n'


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


del n
m = s.format_map(safesub(vars()))
print(m)

import sys


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'yangyang'
n = 21
print(sub('Hello {name}'))
print(sub('You have {n} message.'))
print(sub('You favorite color is {color}'))

# -------------------------------------#

import string

name = 'hongsong'
n = 24
s = string.Template('$name has $n message.')
print(s.substitute(vars()))
