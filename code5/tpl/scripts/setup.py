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
    def enter_setup(self):
        self._driver(resourceId="com.signway.droidkeda:id/btn_set_up").click()
        if self._driver(resourceId="com.signway.droidkeda:id/rl_setting_title").wait.exists(timeout=10000):
            self._logger.debug("enter setting view success")
            return True
        else:
            self._logger.error("enter setting view faile")
            return False

    def check_voice(self):
        self._driver.click(690, 114)
        time.sleep(1)
        level_1 = self._driver(resourceId="com.signway.droidkeda:id/tv_seekbar_voice").text
        self._driver.click(930, 114)
        level_2 = self._driver(resourceId="com.signway.droidkeda:id/tv_seekbar_voice").text
        time.sleep(1)
        if level_1 != level_2:
            self._logger.debug("voice set OK")
            return True
        else:
            self._logger.error("voice set error")
            return False

    def check_auto_sleep(self):
        pass

    def check_screen_protect_time(self):
        pass

    def check_wifi(self):
        pass 

    def check_soft_update(self):
        pass

    def check_about_us(self):
        pass

class Cases(unittest.TestCase):
    def setUp(self):
        self._common = Common()
    
        self._driver = self._common.get_driver()
        self._logger = self._common.get_logger()
        self._driver.press.home()
        time.sleep(1)

    def tearDown(self):
        pass

    def test_check_setting_menus(self):
        
        if self._common.enter_setup() and self._common.check_voice() \
            and True:
            self._logger.debug("success!!!")
        else:
            self._common.save_image()
            exit(-1)


        