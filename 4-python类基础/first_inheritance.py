#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 用class来声明Person是一个类
# 类名：驼峰命名规则,例如： MyNewClass

class Person(object):
    def __init__(self, name, age, gender, nationality='china'):
        """
        类初始化函数

        1 实例化对象时被调用，完成以下参数的初始化
        2 self.args：可以被其他方法引用
        3 self._args: 私有属性
        """
        self._name = name
        self._age = age 
        self._gender = gender 
        self._nationality = nationality
    
    def get_name(self):
        """
        实例方法

        1 必须先实例化一个对象，用这个对象来调用此方法
        2 类不可以直接调用
        """
        return self._name 

    def get_nationality(self):
        return self._nationality

    def set_age(self, age):
        self._age = age

class Programmer(Person):
    # def __init__(self, code, name, age, gender, nationality='china'):
    #     Person.__init__(self, name, age, gender, nationality='china')
    pass
ljz = Programmer('python''lijinzhou', '18', 'man')
print ljz.get_name()
print ljz.get_nationality()


class SuperStar(Person):
    def song(self):
        print "我会唱歌"