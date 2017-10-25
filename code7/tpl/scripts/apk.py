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
    def switch(self, k=True):
        print "init",self.get_light_status()
        self._driver(resourceId="com.signway.droidkeda:id/btn_lighting").click()
        self._driver.delay(2)
        after_click_status = self.get_light_status()
        print "after click:", after_click_status
 
        # turn on
        if k:
            if after_click_status and self.find_image("light_on.png"):
                self._logger.debug("turn on success")
                return True
            else:
                self._logger.error("turn on failed")
                self.save_image()
                return False

        # turn off
        if not k:
            if (not after_click_status) and self.find_image("light_off.png"):
                self._logger.debug("turn off success")
                return True
            else:
                self._logger.error("turn off failed")
                self.save_image()
                return False

    def get_light_status(self):
        return self.get_status(self._driver(resourceId="com.signway.droidkeda:id/btn_lighting"), "selected")

    def find_image(self, image_name):
        media_path = os.path.join(os.environ.get("base_path", "../"),"media")
        # print media_path
        return self._driver.exists(os.path.join(media_path, image_name))


class Cases(unittest.TestCase):
    def setUp(self):
        self._common = Common()
        self._driver = self._common.get_driver()
        self._logger = self._common.get_logger()
        
        self._base_path = os.environ.get("base_path", "../")
        self._media_path = os.path.join(self._base_path, "media")
        self._light_on_pic = os.path.join(self._media_path, "light_on.png")
        self._light_off_pic = os.path.join(self._media_path, "light_off.png")

    def tearDown(self):
        pass

    def test_switch_on_off(self):
        if self._common.get_light_status(): # 初始化为开
            self._common.switch(k=False) and self._common.switch(k=True)
        else: # 初始化为关
            self._common.switch(k=True) and self._common.switch(k=False)

    def test_light_switch(self):
        light_obj = self._driver(resourceId="com.signway.droidkeda:id/btn_lighting")
        light_statu = self._common.get_status(light_obj, "selected")
        self._logger.debug(light_statu)
        if light_statu:
            if self._driver.exists(self._light_on_pic):
                self._logger.debug("light status is on")
                light_obj.click()
                self._driver.delay(1)

                after_click_light_statu = self._common.get_status(light_obj, "selected")
                self._logger.debug(after_click_light_statu)
                if after_click_light_statu == False and self._driver.exists(self._light_off_pic):
                    self._logger.debug("turn off light success")

                    light_obj.click()
                    self._driver.delay(1)
                    after_second_click_light_statu = self._common.get_status(light_obj, "selected")
                    if after_second_click_light_statu and self._driver.exists(self._light_on_pic):
                        self._logger.debug("turn on light success")
                    else:
                        self._logger.error("turn on light failed")
                        exit(-1)
                else:
                    self._logger.error("turn off light failed")
                    self._common.save_image()
                    exit(-1)
            else:
                self._logger.error("status is True, display on, Not math")
                self._common.save_image()
                exit(-1)

        if not light_statu:
            if self._driver.exists(self._light_off_pic):
                self._logger.debug("light status is off")
                light_obj.click()
                self._driver.delay(1)

                after_click_light_statu = self._common.get_status(light_obj, "selected")
                if after_click_light_statu and self._driver.exists(self._light_on_pic):
                    self._logger.debug("turn on light success")

                    light_obj.click()
                    self._driver.delay(1)
                    after_second_click_light_statu = self._common.get_status(light_obj, "selected")
                    self._logger.debug(after_click_light_statu)
                    if after_second_click_light_statu == False and self._driver.exists(self._light_off_pic):
                        self._logger.debug("turn off light success")
                    else:
                        self._logger.error("turn off light failed")
                        exit(-1)
                else:
                    self._logger.error("turn on light failed")
                    self._common.save_image()
                    exit(-1)
            else:
                self._logger.error("status is False, display off, Not math")
                self._common.save_image()
                exit(-1)
            