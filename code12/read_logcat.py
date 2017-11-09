#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

# 11-09 12:13:54.566  3073  3073 E AndroidRuntime: FATAL EXCEPTION: main
# 11-09 12:13:54.566  3073  3073 E AndroidRuntime: Process: com.example.crashtest, PID: 3073

regex = ".*Process: (com.*), PID.*"

with open("/Users/lijinzhou/Desktop/xinweishitong/code/logcat.log", "r") as f:
    while True:
        line = f.readline()
        if "FATAL EXCEPTION: main" in line:
            line = f.readline()
            package_name = re.match(regex, line)
            if package_name:
                package_name = package_name.group(1)
                print package_name
                break

# with open("/Users/lijinzhou/Desktop/xinweishitong/code/logcat.log", "r") as f:
#     content = f.readlines()
#     print type(content)
#     nums = content.count("error")
#     nums = 0 
#     for line in content:
#         nums += line.lower().count("error")
#         # nums += line.count("Error")
#         # nums += line.count("ERROR")
#     print nums

