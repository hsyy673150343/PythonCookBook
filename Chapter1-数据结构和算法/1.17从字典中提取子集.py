#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/25 19:56
# @Author   : 洪松
# @File     : 1.17从字典中提取子集.py

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)


tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}

p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)
p2 = {key: prices[key] for key in prices.keys() & tech_names}
print(p2)