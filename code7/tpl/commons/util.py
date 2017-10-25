#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import time

import atx

from mylogging import log


class Util(object):

    LOG_PATH = os.environ.get("case_log_final_path", './')

    def __init__(self):
        self._driver = atx.connect(os.environ.get('device'), '')
        self._logger = log

    def get_driver(self):
        return self._driver

    def get_logger(self):
        return self._logger

    def get_bouns(self, obj):
        return self.get_status(obj, "bounds")

    def _get_element_point(self, obj, point):
        data = self.get_bouns(obj)
        return data.get(point)

    def get_element_top_y(self, obj):
        return self._get_element_point(obj, "top")

    def get_element_bottom_y(self, obj):
        return self._get_element_point(obj, "bottom")

    def get_element_left_x(self, obj):
        return self._get_element_point(obj, "left")

    def get_element_right_x(self, obj):
        return self._get_element_point(obj, "right")

    def get_element_center_x(self, obj):
        return (self.get_element_center_x(obj) + self.get_element_right_x(obj))/2

    def get_element_center_y(self, obj):
        return (self.get_element_bottom_y(obj) + self.get_element_top_y(obj))/2

    def is_package_exists(self, app_package, timeout=3000):
        if self._driver(packageName=app_package).wait.exists(timeout=timeout):
            return True
        else:
            return False

    def start_app(self, app_package):
        self._driver.start_app(app_package)
        if self.is_package_exists(app_package, timeout=5000):
            return True
        else:
            return False

    def stop_app(self, app_package):
        self._driver.stop_app(app_package)
        time.sleep(1)
        if self.is_package_exists(app_package, timeout=2000):
            return False
        else:
            return True

    def get_current_time(self):
        return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    def save_image(self):
        self._driver.screenshot(os.path.join(self.LOG_PATH, self.get_current_time()+".png"))

    def get_status(self, objs, status_key):
        """
        { u'contentDescription': u'',
            u'checked': False,
            u'scrollable': False,
            u'text': u'Settings',
            u'packageName': u'com.android.launcher',
            u'selected': False,
            u'enabled': True,
            u'bounds': {u'top': 385,
                        u'right': 360,
                        u'bottom': 585,
                        u'left': 200},
            u'className': u'android.widget.TextView',
            u'focused': False,
            u'focusable': True,
            u'clickable': True,
            u'chileCount': 0,
            u'longClickable': True,
            u'visibleBounds': {u'top': 385,
                                u'right': 360,
                                u'bottom': 585,
                                u'left': 200},
            u'checkable': False
            }
        """
        return objs.info.get(status_key)
    

    