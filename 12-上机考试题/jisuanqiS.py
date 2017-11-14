#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : Calculator.py
# Author        : Ljz
# Created       : 30th December 2016
# Last Modified : 30th December 2016
# Version       : 2.0
# 
# Description   : Calculate the N number of add, subtract, multiply and divide
#*****************************************************************************

from __future__ import division
import re
import sys

mydict = {'*':{'operation':lambda x,y:x*y,'level':2},
'/':{'operation':lambda x,y:x/y,'level':2},
'+':{'operation':lambda x,y:x+y,'level':1},
'-':{'operation':lambda x,y:x-y,'level':1}}

# 匹配运算公式
pattern = "^(\d+|\d+\.\d+)([\+\*/-](\d+|\d+\.\d+))+$"

def check_input(user_input):
    user_input = user_input.replace(" ", "")
    print user_input
    if user_input.lower()=="n": # 输入n 退出
        return (True,"exit")
    elif user_input.find("/0")>-1: # 分母为0处理
        return (False,"division is 0")
    elif re.match(pattern, user_input):
        return (True, "")
    else:
        return (False,"input error") # 非法输入处理

def jisuan(user_input):
    ele = re.split("([\+\*/-])",user_input) # 把用户的输入转换成列表
    ele.reverse() # 反转列表，以便于顺序出栈
    op=[] # 暂时存放出栈的操作符
    num=[] # 暂时存放出栈的数字

    while True:
        item = ele.pop() # 从列表中取出一个元素
        if item not in mydict.keys(): # 若取出的元素为数字，加入num列表
            num.append(float(item))
        else: # 取出元素为运算符
            if len(op)>0: #若op列表有元素
                if mydict[item]['level'] > mydict[op[0]]['level']: # 取出的运算符优先级高
                    first_num  = num.pop()
                    second_num = float(ele.pop())
                    op_type    = item
                    op_result = mydict[op_type]['operation'](first_num, second_num)
                    num.append(op_result)
                else: # op列表里的运算符优先级高
                    second_num = num.pop()
                    first_num  = num.pop()
                    op_type    = op.pop()
                    op_result = mydict[op_type]['operation'](first_num, second_num)
                    num.append(op_result)
                    op.append(item)
            else:
                op.append(item)

        if len(ele)==0: # ele元素取完
            second_num = num.pop()
            first_num  = num.pop()
            op_type    = op.pop()

            op_result = mydict[op_type]['operation'](first_num, second_num)
            num.append(op_result)
            return num[0]


if __name__=="__main__":
    while True:
        user_input=raw_input("Formula : ") # 用户输入

        ret=check_input(user_input)
        if ret[0]:
            if ret[1] == "exit":
                sys.exit(0)
        else:
            if not ret[0]:
                print ret[1]
                continue

        result =  jisuan(user_input) # 进行计算并返回计算结果
        print "Result  :",result,'\n'
