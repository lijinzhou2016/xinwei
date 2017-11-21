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

    def switch_auto_time(self, action="off"):
        if action == "off" and self._driver(text="关闭").exists:
            self._logger.debug("Already closed")
            return True
        
        if action == "on" and self._driver(text="开启").exists:
            self._logger.debug("Already opened")
            return True

        self._driver(text="同步时间").click()
        if self._driver(text="前往设置页面").wait.exists(timeout=3000):
            self._driver.delay(1)
            self._driver(text="确定").click()
        else:
            self._logger.error("确认窗口弹出失败")
            return False

        if self._driver(text="设置日期和时间").wait.exists(timeout=5000):
            self._driver.delay(1)
            state = self.get_status(self._driver(textContains="自动确定日期和时间"), "checked")
            self._driver(textContains="自动确定日期和时间").click()
            self._driver.delay(2)
            after_click_state = self.get_status(self._driver(textContains="自动确定日期和时间"), "checked")
            if state == after_click_state:
                self._logger.error("{0} auto update time failed".format("close" if state else "open"))
                return False
            else:
                self._logger.debug("{0} auto update time success".format("close" if state else "open"))
            self._driver(text="下一步").click()
            self._driver.delay(1)
            return True
        else:
            self._logger.error("Enter switch view failed")
            return False


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
