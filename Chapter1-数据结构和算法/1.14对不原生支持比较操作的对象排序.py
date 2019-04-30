#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/25 17:07
# @Author   : 洪松
# @File     : 1.14对不原生支持比较操作的对象排序.py


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print(users)

sort_id = sorted(users, key=lambda u: u.user_id)
print(sort_id)


from operator import attrgetter

sort_id = sorted(users, key=attrgetter('user_id'))
print(sort_id)

min_id = min(users, key=attrgetter('user_id'))
print(min_id)

max_id = max(users, key=attrgetter('user_id'))
print(max_id)