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
        # self._driver.click(768,428)
        self._driver(resourceId="com.signway.droidkeda:id/btn_set_up").click()
        self._driver.delay(3)
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
        obj = self._driver(resourceId="com.signway.droidkeda:id/tb_auto_sleep")
        status = self.get_status(obj, "checked")
        print status
        if not status: # 关闭状态
            print "begin turn on"
            obj.click()
            
            if self._driver(resourceId="com.signway.droidkeda:id/iv_ok").wait.exists(timeout=5000):
                # {u'bottom': 363, u'left': 417, u'right': 497, u'top': 193}
                # b_y = 363
                # x = (417+497)/2
                time_btn = self._driver(resourceId="com.signway.droidkeda:id/pv_minute")
                time_zuobiao = self.get_status(time_btn, "bounds")
                y_middle = (time_zuobiao.get("bottom") + time_zuobiao.get("top"))/2
                y = time_zuobiao.get("bottom")
                x = (time_zuobiao.get("left") + time_zuobiao.get("right"))/2
                
                self._driver.swipe(x,y_middle, x, y)
                
                self._driver.delay(1)
                self._driver(resourceId="com.signway.droidkeda:id/iv_ok").click()
                self._driver.delay(1)
            if self.get_status(obj, "checked"): # 判断是否打开成功
                self._logger.debug("turn on auto sleep success")
                return True
            else:
                self._logger.error("turn on auto sleep failed")
                return False
        else:
            print "begin turn off"
            obj.click()
            self._driver.delay(1)
            if not self.get_status(obj, "checked"): # 判断是否关闭成功
                self._logger.debug("turn off auto sleep success")
                return True
            else:
                self._logger.error("turn off auto sleep failed")
                return False


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

    def tearDown(self):
        # self._driver.press.home()
        self._driver(resourceId="com.signway.droidkeda:id/iv_return").click()

    def test_check_setting_menus(self):
        if not(self._common.enter_setup() and self._common.check_auto_sleep()):
            self._common.save_image()
