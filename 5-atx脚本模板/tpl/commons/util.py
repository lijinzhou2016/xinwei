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
    

    