#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_LIST_PATH = os.path.join(BASE_PATH, 'caselist')
MEDIA_PATH = os.path.join(BASE_PATH, 'media')
COMMONS_PATH = os.path.join(BASE_PATH, 'commons')
sys.path.append(BASE_PATH)

import setting

# root/20171010131313/LOOP_1/cal.android.one_and_one/loop_1
case_file = os.path.join(CASES_LIST_PATH, setting.CASES_LIST)
start_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
case_lines = ''
log_root_path = os.path.join(setting.LOG_PATH,  )

os.environ.setdefault("base_path", BASE_PATH)

#设置设备号环境变量
os.environ.setdefault("device", setting.DEVICE)
# 读取case集
with open(case_file) as f:
    case_lines = f.readlines()


for big_loop in range(setting.CASES_LOOP):
    big_loop_path = os.path.join(log_root_path, "LOOP_"+str(big_loop+1))
    os.makedirs(big_loop_path)
    for line in case_lines:
        if line.strip().startswith("#") or len(line.strip()) < 3:
            continue
        if "," not in line or line.count(",") > 1:
            print "!!! please check this line:", line
            continue

        try:
            line = line.replace("\n","").strip()
            case = line.split(",")[0].strip()
            loop = int(line.split(",")[1].strip())
            cmd = 'python -m unittest ' + case
            case_log_path = os.path.join(big_loop_path, case)
            os.makedirs(case_log_path)
            for i in range(loop):
                try:
                    case_log_final_path = os.path.join(case_log_path, "loop_"+str(i+1))
                    os.makedirs(case_log_final_path)
                    os.environ.setdefault("case_log_final_path", case_log_final_path)
                    os.environ.setdefault("case_name", case)

                    if setting.GET_LOGCAT:
                        pass
                        # 创建新线程收集logcat
                        # os.system("adb logcat>test.log")
                    current_case = case + " - " + str(big_loop+1) + " - " + str(i+1)
                    with open("current_case.txt", 'w') as f:
                        f.write(current_case)

                    print "="*5, current_case, "="*5    
                    os.system(cmd) # 执行测试用例
                    os.environ.pop("case_log_final_path")
                    os.environ.pop("case_name")
                    if setting.GET_LOGCAT:
                        pass
                except BaseException, e:
                    print e 
                    print "!!! please check this line:", line
        except BaseException, e:
            print e
            print "!!! please check this line:", line

