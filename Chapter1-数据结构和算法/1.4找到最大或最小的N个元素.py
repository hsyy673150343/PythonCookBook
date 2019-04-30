#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:49
# @Author   :洪松
# @File     :1.4找到最大或最小的N个元素.py

import heapq

nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))#[42, 37, 23]
print(heapq.nsmallest(3,nums))#[-4, 1, 2]

portfolio = [
    {'name':'IBM','shares':100,'price':91.9},
    {'name':'AAPL','shares':50,'price':543.22},
    {'name':'FB','shares':35,'price':16.35},
    {'name': 'FA', 'shares': 35, 'price': 14.35},
    {'name': 'FC', 'shares': 35, 'price': 155.35},
    {'name': 'FD', 'shares': 35, 'price': 13.35}
]
cheap = heapq.nsmallest(3,portfolio,key=lambda m:m['price'])
expensive = heapq.nlargest(3,portfolio,key=lambda m:m['price'])
print(cheap)
print(expensive)

nums = [1,8,2,23,7,-4,18,23,42,37,2]
heap = list(nums)
heapq.heapify(heap)
print(heap)#[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
print(heapq.heappop(heap))#-4
print(heapq.heappop(heap))#1
print(heapq.heappop(heap))#2