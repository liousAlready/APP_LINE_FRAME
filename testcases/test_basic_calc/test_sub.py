#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 21:41
# @Author  : limusem
# @File    : test_sub.py
# @Software: PyCharm
# @Description:

import time
import allure
import pytest
from selenium.webdriver.common.by import By


@allure.epic("Google-android计算器")
@allure.feature("V1.0")
class TestSub:

    @allure.story("基本运算模块")
    @allure.title("[case01] 验证计算器能否正常完成减法功能")
    @pytest.mark.baseic
    def test_case_01(self, start_app, stop_app):
        with allure.step("1.启动安卓系统中的计算器"):
            driver = start_app
        with allure.step("2.依次按下 9、+、8、="):
            driver.find_element(By.XPATH, '//android.widget.Button[@text="9"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@text="-"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@text="8"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@text="="]').click()
            time.sleep(1)
        with allure.step("3.验证实际结果是否正确"):
            result = driver.find_element(By.XPATH,
                                         '//android.widget.TextView[@resource-id="com.android.calculator2:id/result"]').text
            assert result == "1"
            time.sleep(2)
        with allure.step("4.关闭app"):
            stop_app
