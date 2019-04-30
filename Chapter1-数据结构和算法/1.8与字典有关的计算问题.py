#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 20:53
# @Author   :洪松
# @File     :1.8与字典有关的计算问题.py

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
#-----求最小-----#
min_price = min(zip(prices.values(),prices.keys()))
print(min_price)
#-----求最大-----#
max_price = max(zip(prices.values(),prices.keys()))
print(max_price)
#-----排序------#
sorted_price = sorted(zip(prices.values(),prices.keys()))
print(sorted_price)

print(min(prices, key=lambda k: prices[k]))#FB
min_values = prices[min(prices, key=lambda k: prices[k])]
print(min_values)#10.75