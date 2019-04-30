#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 15:23
# @Author   :洪松
# @File     :1.5实现优先级队列.py

import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0
    #heapq.heappush(heap,item):将item，推入heap
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()#实例化对象
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)
print(q.pop())#Item('bar')
print(q.pop())#Item('spam')
print(q.pop())#Item('foo')
print(q.pop())#Item('grok')

