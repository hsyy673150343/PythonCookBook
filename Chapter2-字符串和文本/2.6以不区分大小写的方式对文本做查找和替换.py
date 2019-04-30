#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 17:41
# @Author   : 洪松
# @File     : 2.6以不区分大小写的方式对文本做查找和替换.py
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
res = re.findall('python', text, flags=re.IGNORECASE)
print(res)

res = re.sub('python', 'hs', text, flags=re.IGNORECASE)
print(res)


def matchcase(word):
    def replace_word(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace_word

res = re.sub('python', matchcase('hs'), text, flags=re.IGNORECASE)
print(res)
