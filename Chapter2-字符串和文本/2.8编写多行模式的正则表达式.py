#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 18:04
# @Author   : 洪松
# @File     : 2.8编写多行模式的正则表达式.py

import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
                multiline comment */
'''

print(comment.findall(text1))
print(comment.findall(text2))


comment_1 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment_1.findall(text2))

# re.DOTALL使得正则表达式中的句点可以匹配所有的字符，包括换行符。
comment_2 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment_2.findall(text2))
