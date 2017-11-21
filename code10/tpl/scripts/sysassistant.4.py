#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import unittest
import time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMONS_PATH = os.path.join(BASE_PATH, 'commons')
sys.path.append(COMMONS_PATH)
from util import Util


class Common(Util): 

    def timer_power(self):
        self._driver(text="定时开关机").click()
        self._driver.delay(1)
        if self._driver(text="常开").wait.exists(timeout=3000):
            self._logger.debug("enter  timer power view success")
        else:
            self._logger.error("enter  timer power view failed")
            return False
        
        # 完善，判断
        self._driver(text="统一").click()
        self._driver.delay(1)
        self._driver(text="定时").click()
        self._driver.delay(1)

        # 获取系统时间
        t = self._driver(resourceId="com.signway.assist:id/activity_time").text
        h = t.split(":")[0]
        m = t.split(":")[1]

        self._driver(text="开启").click()
        self._driver.delay(1)
        self._driver(text="开始时间").click()
        self._driver.delay(1)

        for loop in range(int(h)):
            self._driver(resourceId="com.signway.assist:id/add").click()
        
        for loop in range(int(m)+5):
            self._driver(resourceId="com.signway.assist:id/add", instance=1).click()

        self._driver(text="确定").click()
        self._driver.delay(1)

        self._driver(className="android.widget.ImageView").click()
        self._driver.delay(1)
        self._driver(className="android.widget.ImageView").click()
        self._driver.delay(1)
        self._driver.press.home()

        # 等待关机
        t = 10*60
        for i in range(t):
            time.sleep(1)
            try:
                self._driver.adb_shell("adb devices")
            except BaseException as e:
                self._logger.debug("正在关闭。。。。")
                break

        for i in range(t):
            time.sleep(1)
            try:
                os.system("adb connect 192.168.0.133:5566")
                time.sleep(1)
                self._driver.adb_shell("adb devices")
                self.start_assistant()
                time.sleep(1)
                tt = self._driver(resourceId="com.signway.assist:id/activity_time").text
                print tt
                return
                # if int(tt.split(":")[1]) - int(t.split(":")[1]) == 5
            except BaseException as e:
                pass


    def start_assistant(self):
        """启动系统助手

        从主界面点击菜单，进入二级界面，点击应用图标启动
        """

        self._driver.press.home()
        self._driver.delay(1)
        self._driver(description="应用").click()
        
        if self._driver(text="系统助手").wait.exists(timeout=5000):
            self._driver.delay(1)
            self._driver(text="系统助手").click()
            if self._driver(text="调整分辨率").wait.exists(timeout=5000):
                self._logger.debug("Start assistant success")
                return True
            else:
                self._logger.error("Start assistant failed")
                return False
        else:
            self._driver.error("Not found assistant App")
            return False


class Cases(unittest.TestCase):
    def setUp(self):
        self._common = Common()
        self._driver = self._common.get_driver()
        self._logger = self._common.get_logger()

    def tearDown(self):
        self._driver.stop_app("com.signway.assist")
        self._driver.press.home()
