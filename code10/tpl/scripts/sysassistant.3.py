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
    
    def screen_rotate(self):
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

 