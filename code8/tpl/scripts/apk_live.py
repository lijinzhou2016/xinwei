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
    def switch(self, action):
        """turn on/off the light

            action=True: 打开
            action=False: 关闭
        """
        status = self.get_light_status() # 点击之前照明灯的状态

        # 若照明灯当前的状态和想要操作后的状态相同，则直接返回
        # 例如，想要关闭，当前就是关闭状态，则不做任何操作直接返回
        if action == status:
            msg = "light already {0}".format("on" if action else "off")
            self._logger.debug(msg)
            return True

        objs = self._driver(resourceId="com.signway.droidkeda:id/btn_lighting")
        objs.click()
        self._driver.delay(1)
        after_status = self.get_light_status() # 点击之后照明灯的状态

        if action: # turn on
            if after_status == True and self.find_image("light_on.png"):
                self._logger.debug("turn on success")
                return True
            else:
                self._logger.error("turn on failed")
                self.save_image()
                return False

        if not action: # turn off
            if after_status == False and self.find_image("light_off.png"):
                self._logger.debug("turn off success")
                return True
            else:
                self._logger.error("turn off failed")
                self.save_image()
                return False

    def get_light_status(self):
        """获取当前照明灯的打开状态

            True: 打开
            False: 关闭
        """
        objs = self._driver(resourceId="com.signway.droidkeda:id/btn_lighting")
        return self.get_status(objs, "selected")

    def find_image(self, file_name):
        """判断传入的图片在当前页面是否存在

            return True/False
        """
        return self._driver.exists(self.get_image_abs_path(file_name))

    def get_image_abs_path(self, file_name):
        media_path = os.path.join(os.environ.get("base_path", "../"),"media")
        print os.path.join(media_path, file_name)
        return os.path.join(media_path, file_name)

    def turn(self, level, action):
        print level, action

        data = {
            1:{"on":"fengshan_1_on.png", "off":"fengshan_1_off.png"},
            2:{"on":"fengshan_2_on.png", "off":"fengshan_2_off.png"},
            3:{"on":"fengshan_3_on.png", "off":"fengshan_3_off.png"},
        }

        if self.find_image(data.get(level).get(action)):
            msg = "fengshan already level: {0}, status: {1}".format(str(level), action)
            self._logger.debug(msg)
            return True 
        else:
            if action == "on":
                icon = data.get(level).get("off")
            else:
                icon = data.get(level).get("on")

            icon_path = self.get_image_abs_path(icon)

            # print icon_path
            self._driver.click_image(icon_path)

            self._driver.delay(2)
            if self.find_image(data.get(level).get(action)):
                msg = "turn fengshan level: {0}, status: {1} success".format(str(level), action)
                self._logger.debug(msg)
                return True
            else:
                msg = "turn fengshan level: {0}, status: {1} failed".format(str(level), action)
                self._logger.error(msg)
                self.save_image()
                return False


class Cases(unittest.TestCase):
    def setUp(self):
        # self._common调用 util.py里面封装的接口
        self._common = Common()
        # self._driver调用atx提供的接口
        self._driver = self._common.get_driver()
        self._logger = self._common.get_logger()

        # self._driver(resourceId="com.signway.droidkeda:id/btn_set_up").click()
        # self._driver.delay(10)
        # exit(0)

    def tearDown(self):
        pass

    def test_switch_light(self):
        self._common.switch(action=True)
        self._common.switch(action=False)

    def test_switch_fengshan(self):

        self._common.turn(1, 'on')
        self._common.turn(1, 'off')
        self._common.turn(2, 'on')
        self._common.turn(2, 'off')
        self._common.turn(3, 'on')
        self._common.turn(3, 'off')
