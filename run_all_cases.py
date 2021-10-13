#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 20:54
# @Author  : limusem
# @File    : run_all_cases.py
# @Software: PyCharm
# @Description:


import os
import pytest

current_path = os.path.dirname(os.path.abspath(__file__))
json_report_path = os.path.join(current_path, "report", "json")
html_report_path = os.path.join(current_path, "report", "html")

pytest.main(['-s', '-v', '--alluredir=%s' % json_report_path, '--clean-alluredir'])
os.system('allure generate %s -o %s --clean' % (json_report_path, html_report_path))
