#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 21:08
# @Author  : limusem
# @File    : conftest.py
# @Software: PyCharm
# @Description:

import time
import pytest

from appium import webdriver

driver = None


@pytest.fixture()
def start_app(android_setting):
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', android_setting)

    return driver


@pytest.fixture()
def stop_app():
    yield driver
    time.sleep(2)
    driver.close_app()
