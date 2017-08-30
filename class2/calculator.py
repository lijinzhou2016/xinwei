#!/usr/bin/env python
# coding: utf-8

"""
以 Pixel虚拟机 为例

计算 1 + 2 = 3
"""

from uiautomator import Device

driver = Device()

# 不同设备，这两个变量值有所不同
calculator_package = "com.android.calculator2"
calculator_activity = ".Calculator"

# 启动计算器
#driver.shell_adb("shell am start -n 'com.android.calculator2/.Calculator'")
driver.start_activity(calculator_package, calculator_activity)
driver.delay(3)

driver(resourceId="com.android.calculator2:id/digit_1").click()  # click 1
driver.delay(1)
driver(resourceId="com.android.calculator2:id/op_add").click()  # click +
driver.delay(1)
driver(resourceId="com.android.calculator2:id/digit_2").click()  # click 2
driver.delay(1)
driver(resourceId="com.android.calculator2:id/eq").click()  # click =
driver.delay(3)

if driver(resourceId="com.android.calculator2:id/formula").get_text() == "3":
    print "success"
else:
    print "faile"

driver.press.home()
