#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/25 15:34
# @Author   : 洪松
# @File     : 1.12找出序列中出现次数最多的元素.py

from collections import Counter

words = ['hs', 'yy', 'hs', 'hs', 'hs', 'yy', 'hs', 'hs', 'hh', 'mm', 'ii']
word_counts = Counter(words)
top_two = word_counts.most_common(2)
print(top_two)

#手动计数

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes','hs']


# for word in morewords:
#     word_counts[word] += 1

# print(word_counts['hs'])


# word_counts.update(morewords)
# print(word_counts)


a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

c = a + b
print(c)

d = a - b
print(d)