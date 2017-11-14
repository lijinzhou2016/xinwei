#!/usr/bin/env python
# coding:utf-8

import os, sys
import unittest
import atx
from uiautomator import Device

"""
resource-id   - resourceId, resourceIdMatches
text          - text, textContains, textMatches, textStartsWith
class         - className, classNameMatches
content-desc  - description, descriptionContains, descriptionMatches, descriptionStartsWith
package       - packageName, packageNameMatches
index         - index, instance

"""

class Cases(unittest.TestCase):

    def setUp(self):
        self._driver = atx.connect()
        self._device = Device()

    def test_click(self):
        self._driver.click(540, 1650)
        self._driver.delay(2)
        self._driver.press.home()
        # self._driver.press("home")
        self._driver.delay(1)
        self._driver(description="Apps").click()
        self._driver.delay(1)
        self._driver.press.back()
        # self._driver.press("back")
        self._driver(text="Settings").long_click()

    def test_press(self):
        """press:

            home, back, left, right, up, down, 
            center, menu, search, enter, delete(or del), 
            recent, volume_up, volume_down, camera, power
        """

        self._driver.press.volume_down()
        self._driver.delay(1)
        self._driver.press.volume_down()
        self._driver.delay(1)
        self._driver.press.volume_up()
        self._driver.delay(1)

    def test_screen(self):
        self._device.screen.off()
        self._driver.delay(2)
        self._device.screen.on()
        self._driver.delay(2)
        self._device.sleep()
        self._driver.delay(2)
        self._device.wakeup()

    def test_image(self):
        self._driver.start_app("com.android.calculator2")
        self._driver.delay(2)
        image_path = os.path.dirname(os.path.abspath(__file__))
        if self._driver.exists(os.path.join(image_path, "1.jpg")):
            self._driver.click_image(os.path.join(image_path, "1.jpg"))
            self._driver.delay(1)
        else:
            print "Not find image"

        self._driver.screenshot("ttt.png")

        self._driver.stop_app("com.android.calculator2")

    def test_wait(self):
        if self._driver(text="1").wait.exists(timeout=10000):
            print "find it"
        
        if self._driver(text="1").wait.gone(timeout=10000):
            print "it gone"

    def test_child(self):
        self._driver(className="android.view.ViewGroup").child(text="Phone").click()
        self._driver.delay(1)
        self._driver.press("home")
        self._driver.delay(1)

        self._driver(text="Phone").click()
        self._driver.delay(1)
        self._driver.press("back")

    def test_instance(self):
        # count, instance
        # count = self._driver(className="android.widget.TextView").count
        # print count
        # self._driver(className="android.widget.TextView", instance=7).click()
        # self._driver.press.home()
        # self._driver.delay(1)
        # self._driver(className="android.widget.TextView")[7].click()

        # 计算器遍历
        objs = self._driver(className="android.widget.Button")
        for obj in objs:
            obj.click()

    def test_set_text(self):
        # self._driver(resourceId="com.android.messaging:id/recipient_text_view").set_text("10086")
        # self._driver.delay(1)
        # self._driver.press.enter()
        # self._driver(resourceId="com.android.messaging:id/recipient_text_view").clear_text()
        # self._driver.delay(1)
        # self._driver.type("10086", enter=False)

        self._driver(resourceId="com.android.messaging:id/compose_message_text").long_click()

    def test_drag(self):
        self._driver(text="Settings").drag.to(950, 1000)
        self._driver.delay(1)
        self._driver(text="Settings").swipe.left(steps=100)
        
    def test_swipe(self):
        self._driver.swipe(1000, 1000, 500, 1000, steps=50)
        self._driver.delay(1)
        self._driver.swipe(500, 1000, 1000, 1000, steps=10)
        
    def test_scroll(self): 
        self._driver(scrollable=True).scroll.to(text="Google")
        print "find it"
       
    def test_pinch(self):
        # com.google.android.apps.photos:id/list_photo_tile_view
        self._driver(resourceId="com.google.android.apps.photos:id/list_photo_tile_view").pinch.Out()
        self._driver.delay(1)
        self._driver(resourceId="com.google.android.apps.photos:id/photo_hashtag_fragment_container").pinch.In()

    def test_cmd(self):
        dev = self._driver.adb_cmd("devices")
        mem = self._driver.adb_shell("dumpsys meminfo")
        print dev 
        print mem

    def test_relative(self):
        self._driver(text="Cellular data").right(className="android.widget.Switch").click()
    

