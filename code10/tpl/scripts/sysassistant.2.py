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

    def time_set(self):
        """设置系统时间

        """

        self._driver.delay(1)
        self._driver(text="设置时间").click()
        if self._driver(text="设置系统时间").wait.exists(timeout=5000):
            self._logger.debug("Enter time set view success")
        else:
            self._logger.error("Enter time set view failed")
            return False

        # 若自动同步为开，则关闭
        if not self.switch_auto_time("off"):
            return False

        # 获取当前日期和时间
        date = self._driver(resourceId="com.signway.assist:id/set_system_time_date").child(className="android.widget.TextView", instance=1).text
        time = self._driver(resourceId="com.signway.assist:id/set_system_time_time").child(className="android.widget.TextView", instance=1).text
        print "current - ","date:", date, "time:",time 

        # 修改日期
        self._driver(text="日期").click()
        self._driver.delay(1)
        for add_btn in self._driver(resourceId="com.signway.assist:id/add"):
            add_btn.click()
        self._driver(text="确定").click()
        self._driver.delay(1)


        # 修改时间
        self._driver(text="时间").click()
        self._driver.delay(1)
        for add_btn in self._driver(resourceId="com.signway.assist:id/add"):
            add_btn.click()
        self._driver(text="确定").click()
        self._driver.delay(1)

        after_click_date = self._driver(resourceId="com.signway.assist:id/set_system_time_date").child(className="android.widget.TextView", instance=1).text
        after_click_time = self._driver(resourceId="com.signway.assist:id/set_system_time_time").child(className="android.widget.TextView", instance=1).text
        print "after cick - ","date:", after_click_date, "time:",after_click_time 

        if after_click_date != date and after_click_time != time:
            self._logger.debug("set time success")
        else:
            self._logger.error("set time failed")
            return False

        if self.switch_auto_time("on"):
            # 可能有问题
            self._driver(className="android.widget.ImageView").click()
            self._driver.delay(1)
            return True 
        else:
            return False

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

