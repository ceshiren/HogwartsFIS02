#!/usr/bin/env python
# -*- coding: utf-8 -*-

# yield 生成器 next()来获取生成器里面的下一个值
def provider():
    for i in range(0, 10):
        print("开始操作")
        yield  # 相当于 return i ，同时记录了上一次的执行位置
        print("结束操作")


p = provider()
# print(p)
print(next(p))
print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
#
# for i in p :
#     print(i)
