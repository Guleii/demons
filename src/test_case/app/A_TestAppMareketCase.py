# -*- coding: utf-8 -*-
# coding:utf-8

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

skip_case = False
skip_reason = "调试"


class AppMarketTest(BaseUnittest.BaseTestCase):

    """
        测试应用市场
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_app_market(self):
        search_app = SearchApp(self.driver)
        search_app.start_test_search_app()







if __name__ == "__main__":

    Utils.Logging.error("纸飞机反击反击减肥减肥111")

    time.sleep(10)
    suiteAll = unittest.TestSuite()
    test1 = unittest.TestLoader().loadTestsFromTestCase(AppMarketTest)
    # test2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    suiteAll.addTest(test1)
    runner = HtmlReport.get_generate_report_object()
    runner.run(suiteAll)

    # 发送邮件
    # start_send_email()

