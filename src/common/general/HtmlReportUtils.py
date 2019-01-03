# coding:utf-8
__author__ = 'Alan'
'''
description:生成HTML报告的实例获取
'''
from general.HTMLTestRunner_cn import HTMLTestRunner
from config import GlobalConfig as gl
from general.more_devices.BaseAndroidPhone import *

class HtmlReport:

    """
        获取生成报告的HtmlTestRunner实例
    """
    @staticmethod
    def get_generate_report_object(current_device):
        gl.test_app_more_device_device_identity_prefix = get_device_mac(current_device["deviceName"])+"_"
        report_html = gl.report_path+gl.test_app_more_device_device_identity_prefix+gl.report_name
        gl.report_name = report_html
        print("地址wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww： "+str(report_html))
        runner = HTMLTestRunner(title=gl.html_title, description=gl.html_description, stream=open(report_html, "wb"),
                                verbosity=2, retry=gl.test_case_retry_count, save_last_try=gl.save_last_try_result)
        return runner

    """
            获取生成报告的HtmlTestRunner实例
    """

    @staticmethod
    def get_generate_report_object_one_device():
        report_html = gl.report_path+gl.report_name
        print("地址wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww： " + str(report_html))
        runner = HTMLTestRunner(title=gl.html_title, description=gl.html_description, stream=open(report_html, "wb"),
                                verbosity=2, retry=gl.test_case_retry_count, save_last_try=gl.save_last_try_result)
        return runner


"""

这里的verbosity是一个选项,表示测试结果的信息复杂度，有三个值
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
并且 你在命令行里加入不同的参数可以起到一样的效果
加入 --quiet 参数 等效于 verbosity=0
加入--verbose参数等效于 verbosity=2
什么都不加就是 verbosity=1


在实例化HTMLTestRunner 对象时追加参数，retry，指定重试次数，如果save_last_try 为True ，一个用例仅显示最后一次测试的结果。

"""