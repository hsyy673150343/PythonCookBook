#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 23:59
# @Author   :洪松
# @File     :1.2从任意长度的可迭代对象中分解元素.py

#-----------*式的语法在迭代一个变长的元组序列时尤为有用------------------#

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)


#----------星号表达式在迭代元素为可变长元组的序列时是很有用的。---------#
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
#----------星号表达式在迭代元素为可变长元组的序列时是很有用的。---------#

#----------星号解压语法在字符串操作的时候也会很有用的。比如字符串的分割。---------#
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty/:usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
#----------星号解压语法在字符串操作的时候也会很有用的。比如字符串的分割。---------#

record = ('ACME', 50, 123.45, (12, 18 ,2012))
name, *_, (*_, year) = record
print(name)
print(year)
