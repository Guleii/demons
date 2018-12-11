# coding:utf-8
from general.HtmlReportUtils import HtmlReport
from general.AppLog import *
__author__ = 'Alan'
'''
description:执行测试
'''
import unittest
from general.BaseEmail import *
from config.GlobalConfig import test_case_path,report_name

# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='Test*.py')

# 执行测试
if __name__ == "__main__":
    runner = HtmlReport.get_generate_report_object()
    runner.run(suite)
    start_send_email()  # 发送邮件
