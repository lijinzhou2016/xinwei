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
        media_path = os.path.join(os.environ.get("base_path", "../"),"media")
        return self._driver.exists(os.path.join(media_path, file_name))


class Cases(unittest.TestCase):
    def setUp(self):
        # self._common调用 util.py里面封装的接口
        self._common = Common()
        # self._driver调用atx提供的接口
        self._driver = self._common.get_driver()
        self._logger = self._common.get_logger()

        self._base_path = os.environ.get("base_path", "../")
        self._media_path = os.path.join(self._base_path, "media")
        # 照明灯打开状态图标的路径名
        self._light_on_pic = os.path.join(self._media_path, "light_on.png")
        # 照明灯关闭状态态图标的路径名
        self._light_off_pic = os.path.join(self._media_path, "light_off.png")

    def tearDown(self):
        pass

    def test_switch(self):
        self._common.switch(action=True)
        self._common.switch(action=False)

    def test_light_on_off(self):
        # 照明按钮对象
        light_button_objs = self._driver(resourceId="com.signway.droidkeda:id/btn_lighting")
        # 获取初始化状态：
        # True: 打开
        # False: 关闭
        status = self._common.get_status(light_button_objs, "selected")

        # 初始化为 开
        if status:
            light_button_objs.click() # 点击后，期望为 关
            self._driver.delay(1) 
            after_click_status = self._common.get_status(light_button_objs, "selected") # 获取点击后状态

            # 如果状态为False, 图标为off状态图标，则关闭成功
            if after_click_status == False and self._driver.exists(self._light_off_pic):
                self._logger.debug("turn off success")

                light_button_objs.click() # 点击后，期望为 开
                self._driver.delay(1) 
                after_second_status = self._common.get_status(light_button_objs, "selected") # 获取点击后状态

                # 如果状态为True, 图标为on状态图标，则打开成功
                if after_second_status ==True and self._driver.exists(self._light_on_pic):
                    self._logger.debug("turn on success")
                else:
                    self._logger.debug("turn on failed")
                    self._common.save_image()
            else:
                self._logger.error("turn off failed")
                self._common.save_image()
        else: # 初始化为关
            light_button_objs.click() # on
            self._driver.delay(1) 
            after_click_status = self._common.get_status(light_button_objs, "selected")
            if after_click_status == True and self._driver.exists(self._light_on_pic):
                self._logger.debug("turn on success")

                light_button_objs.click() # off
                self._driver.delay(1) 
                after_second_status = self._common.get_status(light_button_objs, "selected")
                if after_second_status == False and self._driver.exists(self._light_off_pic):
                    self._logger.debug("turn off success")
                else:
                    self._logger.debug("turn off failed")
                    self._common.save_image()
            else:
                self._logger.error("turn on failed")
                self._common.save_image()


        
