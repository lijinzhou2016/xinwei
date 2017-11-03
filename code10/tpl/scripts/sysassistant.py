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

    
    def screen_rotate(self):
        pass

    def timer_power(self):
        self._driver(text="定时开关机").click()
        self._driver.delay(1)
        if self._driver(text="常开").wait.exists(timeout=3000):
            self._logger.debug("enter  timer power view success")
        else:
            self._logger.error("enter  timer power view failed")
            return False
        
        # 完善，判断
        self._driver(text="统一").click()
        self._driver.delay(1)
        self._driver(text="定时").click()
        self._driver.delay(1)

        # 获取系统时间
        t = self._driver(resourceId="com.signway.assist:id/activity_time").text
        h = t.split(":")[0]
        m = t.split(":")[1]

        self._driver(text="开启").click()
        self._driver.delay(1)
        self._driver(text="开始时间").click()
        self._driver.delay(1)

        for loop in range(int(h)):
            self._driver(resourceId="com.signway.assist:id/add").click()
        
        for loop in range(int(m)+5):
            self._driver(resourceId="com.signway.assist:id/add", instance=1).click()

        self._driver(text="确定").click()
        self._driver.delay(1)

        self._driver(className="android.widget.ImageView").click()
        self._driver.delay(1)
        self._driver(className="android.widget.ImageView").click()
        self._driver.delay(1)
        self._driver.press.home()

        # 等待关机
        t = 10*60
        for i in range(t):
            time.sleep(1)
            try:
                self._driver.adb_shell("adb devices")
            except BaseException as e:
                self._logger.debug("正在关闭。。。。")
                break

        for i in range(t):
            time.sleep(1)
            try:
                os.system("adb connect 192.168.0.133:5566")
                time.sleep(1)
                self._driver.adb_shell("adb devices")
                self.start_assistant()
                time.sleep(1)
                tt = self._driver(resourceId="com.signway.assist:id/activity_time").text
                print tt
                return
                # if int(tt.split(":")[1]) - int(t.split(":")[1]) == 5
            except BaseException as e:
                pass




    def system_set(self):
        pass

    def change_px(self):
        pass

    def setup_lvds(self, model="Normal", pipe="单", rgb="8bit", change_pipe="noswap", bk_light="低"):
        self._driver(textContains="Lvds").click()
        time.sleep(1)
        menus_list = [model, pipe, rgb, change_pipe, bk_light]
        for menu in menus_list:
            print "click", menu
            self._driver(text=menu, className="android.widget.TextView").click() 
            # time.sleep(1)
        
        self._driver(resourceId="com.signway.assist:id/window_back_button").click()
        time.sleep(1)
        return True
         

    def look_apk(self):
        pass

    def switch_port(self):
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

    def test_menus(self):
        if self._common.start_assistant() == False:
            self._common.save_image()
            return
        self._common.timer_power()

        # if not self._common.time_set():
        #     self._common.save_image()
        #     return

        # if not self._common.setup_lvds(model="Normal", pipe="单", rgb="8bit", change_pipe="noswap", bk_light="低"):
        #     self._common.save_image()
        #     return

        # if not self._common.setup_lvds(model="Jeida", pipe="双", rgb="6bit", change_pipe="swap", bk_light="高"):
        #     self._common.save_image()
        #     return

