#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import unittest
import time
from mylogging import log
from uiautomator import Device

# 概念：类，方法，模块
#logging
# 主设备待测app包名和activity
# appPackage = 'com.android.calculator2'
# appPackage = "com.meizu.flyme.calculator"
# appActivity = ".Calculator"


class Module:
    def __init__(self, driver):
        self._driver = driver
        self._logger = log

    def start_app(self):
        self._driver.shell_adb("shell am start -n 'com.android.calculator2/.Calculator'")
        if self._driver(resourceId="com.android.calculator2:id/formula").wait.exists(timeout=5000):
            time.sleep(1)
            self._logger.debug("start cal success")
            return True
        else:
            self._logger.error("start cal timeout")
            return False

    
    def cal_two_number(self, formula, expect):
        """
        1+2, 3

        """
        self.clear()

        for op in formula:
            if op is "*":
                op = "×"
            if op is "/":
                op = "÷"
        
            self._driver(text=op).click()
            time.sleep(1)

            # 判断
            self._logger.debug("Input {0} success".format(op))

            # if op in self._driver(resourceId="com.android.calculator2:id/formula").get_text().decode("utf-8"):
            #     self._logger.debug("Input {0} success".format(op))
            # else:
            #     self._logger.error("Input {0} failed".format(op))
            #     return False

        self._driver(text="=").click()
        self._logger.info("Expect: {0}".format(expect))
        time.sleep(2)
        result = self._driver(resourceId="com.android.calculator2:id/formula").get_text()
        
        if result == expect:
            self._logger.info("Result: {0} - Success".format(result))
            return True
        else:
            self._logger.error("Result: {0} - Failed".format(result))
            return False


    def exit_app(self):
        self._driver.shell_adb("shell am force-stop 'com.android.calculator2'")
        self._driver.press.home()
        if not self._driver(resourceId="com.android.calculator2:id/formula").wait.exists(timeout=3000):
            time.sleep(1)
            self._logger.debug("exit cal success")
            return True
        else:
            self._logger.error("exit cal failed")
            return False

    def clear(self):
        if self._driver(resourceId="com.android.calculator2:id/clr").exists:
            self._driver(resourceId="com.android.calculator2:id/clr").click()
            time.sleep(1)
        if not self._driver(resourceId="com.android.calculator2:id/clr").exists:
            self._logger.debug('clear success')
            return True
        else:
            self._logger.error('clear failed')
            return True


class AndroidTestCases(unittest.TestCase):
    def setUp(self):
        self._logger = log
        self._driver = Device()
        # self._sdriver=Device("")
        self._mdriver = Module(self._driver)
        if not self._mdriver.start_app():
            exit(-1)

    def tearDown(self):
        if not self._mdriver.clear():
            exit(-1)
        if not self._mdriver.exit_app():
            exit(-1)


    def test_one_plus_two(self):
        if not self._mdriver.cal_two_number("1+2", "3"):
            exit(-1)

    def test_two_mult_three(self):
        if not self._mdriver.cal_two_number("2*3", "6"):
            exit(-1)

    def test_four_mult_three(self):
        if not self._mdriver.cal_two_number("4*3", "12"):
            exit(-1)

    def test_15(self):
        if not self._mdriver.cal_two_number("5*3", "15"):
            exit(-1)
