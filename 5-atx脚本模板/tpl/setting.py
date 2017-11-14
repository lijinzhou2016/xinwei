#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# 设备号，
# 当电脑连接多台设备时，必须填写
# 当只有一台设备时，可以为空字符串
DEVICE = ''

# 收集logcat日志，未实现
# True: 打开
# False: 关闭收集
GET_LOGCAT = False

# log保存根路径
# 若为空，则保存在tpl目录
LOG_PATH = '/Users/lijinzhou/Desktop/log'

# 需要测试的cases集
CASES_LIST = 'mini.txt'

# 整个测试集循环次数
CASES_LOOP = 1