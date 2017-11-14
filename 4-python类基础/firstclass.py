#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 用class来声明Person是一个类
# 类名：驼峰命名规则,例如： MyNewClass
# object 基类
# class Person: 经典类
# 作用域


# _xx 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。
# 若内部变量标示，如： 当使用“from M import”时，不会将以一个下划线开头的对象引入 。
# __xx 双下划线的表示的是私有类型的变量。只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量）

class Person(object):
    # 类属性，可以直接使用类名来引用，而不需要实例化
    color = '黄种人'
    
    def __init__(self, name, age, gender, nationality='china'):
        """
        类初始化函数

        1 实例化对象时被调用，完成以下参数的初始化
        2 self.args：可以被其他方法引用
        *** 3 self._args: 私有属性, 改为 受保护的属性更准确
        4 定义类属性，通常定义为 self._args
        """
        self._name = name
        self._age = age 
        self._gender = gender 
        self._nationality = nationality
        self.eyes_num = 2
        

    def __my_func_1(self):
        print "你们看不到我"

    def _my_func_2(self):
        print "还可以看到"

    def say_hello(self):
        return self.get_name(), "say hello"
    
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

    # def get_age(self):
    #     return self.__age

    @classmethod
    def say(cls):
        """
        类方法

        1 约定第一个参数为 cls
        2 用 @classmethod 来装饰
        3 可以直接使用类名来引用，而不需要实例化
        """
        return "I am a person"


# 类方法和属性可以直接访问，不需要实例化
print Person.color
print Person.say()
# print Person.get_nationality()
print '-----------------'

# 实例化一个对象xidada
# 此时 xidada 这个参数传给self
xidada = Person('习大大', '60', '男')
print xidada.say()
print xidada.get_name()
print xidada.get_nationality()
print xidada.color
print xidada.eyes_num
print '-----------------'

# 实例对象对类属性的修改，是否影响类
xidada.color = 'white'
print Person.color
print "####",xidada.color

print '-----------------'

# 实例化一个对象 jobs
jobs = Person('乔布斯', '59', '男', nationality='US')
print jobs.say()
print jobs.get_name()
print jobs.get_nationality()
print jobs.color
print jobs.eyes_num
print '-----------------'

# print '.....',jobs._age
# 类属性的修改是否影响实例对象
Person.color = "white"
print jobs.color
