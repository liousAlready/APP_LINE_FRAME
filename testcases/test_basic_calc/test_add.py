#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 21:16
# @Author  : limusem
# @File    : test_add.py
# @Software: PyCharm
# @Description:

import time
import allure
import pytest

from selenium.webdriver.common.by import By


@allure.epic("Google-android计算器")
@allure.feature("V1.0")
class TestAdd:
    @allure.story("基本运算模块")
    @allure.title("[case01] 验证计算器能否正常完成加法功能")
    @pytest.mark.baseic
    def test_case_01(self, start_app, stop_app):
        with allure.step("1.启动安卓系统中的计算器"):
            driver = start_app
        with allure.step("2.依次按下 9、+、8、="):
            driver.find_element(By.XPATH, '//android.widget.Button[@text="9"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@text="+"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@text="8"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@text="="]').click()
            time.sleep(1)
        with allure.step("3.验证实际结果是否正确"):
            result = driver.find_element(By.XPATH,
                                         '//android.widget.TextView[@resource-id="com.android.calculator2:id/result"]').text
            assert result == "17"
            time.sleep(2)
        with allure.step("4.关闭app"):
            stop_app

    @allure.story("基本运算模块")
    @allure.title("[case02] 验证计算器能否正常完成三角函数运算")
    @pytest.mark.baseic
    def test_sin_01(self,start_app,stop_app):
        driver = start_app
        driver.find_element(By.XPATH, '//android.widget.Button[@text="sin"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.widget.Button[@text="π"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.widget.Button[@text="÷"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.widget.Button[@text="2"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.widget.Button[@text=")"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.widget.Button[@text="="]').click()
        time.sleep(2)
        stop_app
