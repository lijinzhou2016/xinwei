#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Dog(object):

    def __init__(self, color, type_, name):
        self._color = color
        self._type_ = type_ 
        self._name = name
        self.__tedian = "haha"
        self.body_heigh = 1
        body_long = 1

    def run(self):
        return "Dog run"
        
    def get_tedian(self):
        return self.__tedian

    def get_name(self):
        return self._name 

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color
    
    # 测试 局部变量 是否可以被内部其他方法调用
    def get_body_log(self):
        return body_long
        

    def __hello(self):
        return "hello world"

# print __name__
# 直接执行此文件：输出__main__
# 被其他文件调用输出 dog

class T(Dog):
    # 测试子类是否会继承父类__XX属性
    def h(self):
        return self.__tedian

if __name__ == "__main__":
    xiaohei = Dog("black", "taidi", "xiaohei")
    print xiaohei._name # 这种调用不报错，但不符合规范
    print xiaohei.body_heigh
    
    # print xiaohei.get_body_log()

    # print xiaohei.__hello()

    # print xiaohei.body_long
    # print xiaohei.__tedian
    # print Dog.body_long

    t=T("red", "taidi","h")
    print t.h()