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

# 主设备待测app包名和activity
appPackage = 'com.android.calculator2'

class Common(Util): 

    def start_calcalator(self):
        if self.start_app(appPackage):
            self._logger.debug("start cal success")
            return True
        else:
            self._logger.error("start cal timeout")
            return False

    def stop_calculator(self):
        self.clear()
        if self.stop_app(appPackage):
            self._logger.debug("exit cal success")
            return True
        else:
            self._logger.error("exit cal failed")
            return False

    def clear(self):
        """清零

        """
        if self._driver(resourceId="com.android.calculator2:id/clr").exists:
            self._driver(resourceId="com.android.calculator2:id/clr").click()
            time.sleep(1)

    def cal(self, formula, expect):
        self.clear()

        # 循环点击输入的内容
        for op in formula:
            if op is "*":
                op = "×"
            if op is "/":
                op = "÷"
            self._driver(text=op).click()
            time.sleep(1)
            self._logger.debug("Input {0} success".format(op))
        self._driver(text="=").click()

        self._logger.info("Expect: {0}".format(expect)) # 打印期望结果
        time.sleep(1)
        result = self._driver(resourceId="com.android.calculator2:id/formula").text # 获取计算结果
        
        if result == expect:
            self._logger.info("Result: {0} - Success".format(result))
            return True
        else:
            self._logger.error("Result: {0} - Failed".format(result))
            return False


class Cases(unittest.TestCase):
    def setUp(self):
        self._common = Common()
        self._driver = self._common.get_driver()
        self._logger = self._common.get_logger()
        self._driver.watcher("AUTO_PRESS_HOME").when(text="Messaging").press("home")
        


    def tearDown(self):
        if not self._common.stop_calculator():
            self._common.save_image()
        self._driver.watchers.remove()

    def test_one_plus_two(self):
        if not self._common.start_calcalator():
            self._common.save_image()
        if not self._common.cal("1+2", "3"):
            self._common.save_image()

    def test_one_plus_one(self):
        if not self._common.start_calcalator():
            self._common.save_image()
        if not self._common.cal("1+1", "3"):
            self._common.save_image()

    def test_watch_api(self):
        
        # self._driver.watcher("AUTO_PRESS_HOME").triggered
        # self._driver.start_app("com.android.messaging")
        self._driver.click(750,1648)
        for i in range(10):
            print i
            time.sleep(2)
            # self._driver.watchers.run()

        
