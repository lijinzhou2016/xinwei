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
    pass


class Cases(unittest.TestCase):
    def setUp(self):
        self._common = Common()
        self._driver = self._common.get_driver()
        self._logger = self._common.get_logger()
        self._get_status = self._common.get_status()


    def test_case_clean(self):
        clean_objs = self._driver(resourceId='com.signway.droidkeda:id/btn_cleaning')
        time_objs = self._driver(resourceId='com.signway.droidkeda:id/tv_cleaning_time') #时间
        status = self.get_status(clean_objs,"selected")

        if status:  # 初始化为 开
            clean_objs.click()
            self._driver.delay(1)
            after_click_status=self._get_status(clean_objs,"selected")
            
            if after_click_status == False:
                self._logger.debug("turn off sucess")

                clean_objs.click()
                self._driver.delay(1)
                after_second_status = self._get_status(clean_objs,"selected")

                if after_click_status == True and time_objs:
                    self._logger.debug("turn on success")
                else:
                    self._logger.debug("turn on failed")

            else:
                self._logger.error("turn off failed")
                self._common.save_image()
        else:  # 初始化为 关
            clean_objs.click()
            self._driver.delay(1)
            after_click_status = self.get_status(clean_objs,"selected")
            if after_click_status == True and time_objs:
                self._logger.debug("turn on success ")
                clean_objs.click()
                self._driver.delay(1)
                after_second_status = self._get_status(clean_objs,"selected")
                if after_second_status == False:
                    self._logger.debug("turn off success")
                else:
                    self._logger.debug("turn off failed")
                    self._common.save_image()
            else:
                self._logger.error("turn on failed")
                self._common.save_image()


        

