#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 22:10
# @Author   :洪松
# @File     :1.3保存最后N个元素.py

from collections import deque
#
# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)
#
# if __name__ == '__main__':
#     with open('E:\hs.txt','r',encoding='utf-8') as f:
#         for line,prevlines in search(f,'哈哈',5):
#             for pline in prevlines:
#                 print(pline,end='')
#             print(line, end='')
#             print('_' * 20)

#-------当有新记录加入而队列已满时会自动移除最老的那条记录-------#
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)#deque([1, 2, 3], maxlen=3)
q.append(4)
q.append(5)
print(q)#deque([3, 4, 5], maxlen=3)
#-------当有新记录加入而队列已满时会自动移除最老的那条记录-------#
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)#deque([1, 2, 3])
q.appendleft(4)
print(q)#deque([4, 1, 2, 3])
print(q.pop())#3
print(q)#deque([4, 1, 2])
