#!/usr/bin/env python
# coding:utf-8

"""
    1 程序调试
    2 日志输出
"""

import logging

# 创建一个logger    
logger = logging.getLogger('mylogger')  
  
# 日志级别
logger.setLevel(logging.INFO) 

# 创建一个handler，用于写入日志文件    
fh = logging.FileHandler('mylogging.log')

# 再创建一个handler，用于输出到控制台    
ch = logging.StreamHandler()

# 定义handler的输出格式formatter   
# format参数中可能用到的格式化串：
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s 用户输出的消息 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)


if __name__ == "__main__":
    logger.debug("debug test")
    logger.info("info test")
    logger.error("error test")