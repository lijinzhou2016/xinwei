#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

def get_input():
    s = raw_input("please input:")
    return s 

# while True:
#     print eval(get_input())

def is_exit(s):
    if "q" == s.lower():
        print "bye~"
        exit(0)

def check(s):
    # encode, decode
    if "/0" in s:
        print u"除数不能为0"
        return False

    return True

def yunsuan(s):
    if "+" in s:
        first_num, second_num = s.split("+")
        sum_ = int(first_num) + int(second_num)
    if "-" in s:
        first_num, second_num = s.split("-")
        sum_ = int(first_num) - int(second_num)
    if "*" in s:
        first_num, second_num = s.split("*")
        sum_ = int(first_num) * int(second_num)
    if "/" in s:
        first_num, second_num = s.split("/")
        sum_ = float(first_num) / float(second_num)
    print sum_


if __name__ == "__main__":
    while True:
        rs = get_input()
        is_exit(rs)
        if check(rs):
            yunsuan(rs)

    