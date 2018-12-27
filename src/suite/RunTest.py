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
import config.GlobalConfig as gl
from src.common.general.more_devices.MoreDevicesUtils import *

# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
# suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='Test*.py')
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='TestLauncher_a_single_*.py')


def run_case_one_device():
    gl.test_app_more_device_device_name = AndroidDebugBridge().get_only_one_device_name()
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    runner = HtmlReport.get_generate_report_object()
    runner.run(suite)
    start_send_email()  # 发送邮件


def run_case_more_devices(current_device):
    runner = HtmlReport.get_generate_report_object(current_device)
    runner.run(suite)
    start_send_email()  # 发送邮件
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)


# 执行测试
if __name__ == "__main__":
    # run_case_one_device()
    if gl.test_app_more_devices:  # 在多个设备上运行测试用例
        start_run_test_with_more_devices_with_accurate()
        # start_run_test_with_more_devices()
        # pass
    else:  # 在单个设备上运行测试用例
        run_case_one_device()

