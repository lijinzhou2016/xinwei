#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 关于logcat： http://blog.csdn.net/tumuzhuanjia/article/details/39555445
# logcat -v threadtime -b all
import os
import subprocess
import sys

# cmd = "adb logcat -v threadtime -b all > logcat.log"
# os.system(cmd)

cmd = "adb logcat -v threadtime -b all"
logcat_stdout = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).stdout

ff = open("logcat.log", "w")

# while True:
#     line = logcat_stdout.readline()
#     ff.write(line)




while True:
    line = logcat_stdout.readline()
    ff.write(line)
    # print line
    if "FATAL EXCEPTION: main" in line:
        print "crash"

        for i in range(10):
            line = logcat_stdout.readline()
            ff.write(line)

        break
ff.close()

