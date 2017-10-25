#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 理解函数 function

# y = 3x + 2
# x = 2, y = 3*2 + 2 =8

# f(x) = 3x + 2
# x = 2, f(2) = 8; f(3) = 11

# 函数定义
def f(x):
    return 3*x + 2

# print f(2) + f(3) 

# 参数
# 函数命名规范：pep8，如下：小写单词加下划线
# 参数可以有默认值
def cal_two_num_sum(first_num, second_num=1):
    print first_num+second_num

# cal_two_num_sum(first_num=1)

def func(*k):
    for i in k:
        print i

# func(1,"char","汉子")


# 内置函数 http://www.runoob.com/python/python-built-in-functions.html
# sum() range() xrange() max() min() sorted()
# p = xrange(10)
# for i in iter(p):
#     print i

def my_max(my_list):
    m = my_list[0]
    for n in my_list:
        if n > m:
            m = n
    return m

# print my_max([1,2,3,4,5,6,4,3,2])
# 作业：自己实现 min(), sum()

