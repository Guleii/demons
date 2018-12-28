# -*- coding: utf-8 -*-
# coding:utf-8
from general.more_devices.BaseAdb import AndroidDebugBridge
from moudle.InputManagerUtils import InputManager

__author__ = 'Alan'
"""
    description:应用市场测试用例
"""

import unittest
# from HTMLTestRunner_cn import HTMLTestRunner
from general import KeyCodeSentUtils, Utils, BaseUnittest
from general.HtmlReportUtils import HtmlReport
from moudle import HomeTabUtils, InputManagerUtils
from src.pages.launcher.LauncherTabPage import *
from src.pages.launcher.LauncherMultiPostersJumpPage import *
from src.pages.launcher.LauncherSingleAppPosterJumpPage import *
from src.pages.launcher.LauncherSingleVideoPosterPage import SingleVideoPoster
from general.ImageContrastUtils import ImageContrast
from config import GlobalConfig as gl
from moudle import HomeTabUtils

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.appMarket.SearchAppPage import SearchApp
from config import DriverConfig

skip_case = True
skip_reason = "调试"


class AppMarketTest(BaseUnittest.BaseTestCase):

    """
        测试应用市场
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_app_market(self):
        search_app = SearchApp(self.driver)
        search_app.start_test_search_app()


    def test_device_size(self):
        time.sleep(4)
        KeyCode.touch_left(self.driver,repeat_count=2)
        time.sleep(3)
        InputManagerUtils.InputManager.input_nine(self.driver)
        # ['1280', '800']
        # widh  = ADB(gl.test_app_more_device_device_name).get_screen_normal_size()
        # Utils.Logging.info("。。。。。。。。。。。。。。。。。。。width:  "+str(widh)+"    high:  ")
        # DriverConfig.init_all_project_by_device_name(AndroidDebugBridge().get_only_one_device_name())







if __name__ == "__main__":
    # DriverConfig.init_all_project_by_device_name(AndroidDebugBridge().get_only_one_device_name())
    # Utils.Logging.error("纸飞机反击反击减肥减肥111")
    #
    # time.sleep(10)
    # suiteAll = unittest.TestSuite()
    # test1 = unittest.TestLoader().loadTestsFromTestCase(AppMarketTest)
    # # test2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    # suiteAll.addTest(test1)
    # runner = HtmlReport.get_generate_report_object()
    # runner.run(suiteAll)
    Utils.Logging.debug("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjjjjjjjjjjj22222222222222jjjjjjjLauncher稳定性测试")
    # DriverConfig.init_all_project_by_device_name(AndroidDebugBridge().get_only_one_device_name())
    DriverConfig.init_all_project_by_device_name(AndroidDebugBridge().get_only_one_device_name())
    InputManager.get_loacation()

    time.sleep(10)
    suiteAll = unittest.TestSuite()
    test1 = unittest.TestLoader().loadTestsFromTestCase(AppMarketTest)
    # test2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    suiteAll.addTest(test1)
    runner = HtmlReport.get_generate_report_object_one_device()
    runner.run(suiteAll)
    # 发送邮件
    # start_send_email()

