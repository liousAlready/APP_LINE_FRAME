#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 20:54
# @Author  : limusem
# @File    : conftest.py
# @Software: PyCharm
# @Description:

import pytest

import time
import os
from appium import webdriver
from appium.webdriver.webdriver import By
from appium.webdriver.common.touch_action import TouchAction


# seesion 整个框架运行一次
@pytest.fixture(scope="session", name="android_setting", autouse=True)
def android_setting():
    des = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "windwos虚拟机",
        "udid": "192.168.67.101:5555",
        "appPackage": "com.android.calculator2",
        "appActivity": "com.android.calculator2.Calculator",
        "noReset": "True"
        # com.android.calculator2 / com.android.calculator2.Calculator
    }
    return des
