# -*- coding: utf-8 -*-
# coding:utf-8

__author__ = 'Alan'
"""
    description:应用管理测试用例
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
from src.pages.appManage.ClearAppDataPage import ClearAppData
from src.pages.appManage.StopAppPage import StopApp
from src.pages.appManage.UninstallAppPage import UninstallApp
from src.pages.appManage.UpdateAppPage import UpdateApp
from src.pages.appManage.AppManageDataConfig import *

skip_case = True
skip_reason = "调试"


class AppManageTest(BaseUnittest.BaseTestCase):

    """
        测试清除应用数据
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_clear_app_data(self):
        clear_app_data = ClearAppData(self.driver)
        clear_app_data.test_clear_app_data()

    """
        测试停止应用
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_stop_app(self):
        stop_app = StopApp(self.driver)
        stop_app.test_stop_app()

    """
        测试卸载应用
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_uninstall_app(self):
        uninstall_app = UninstallApp(self.driver)
        uninstall_app.test_uninstall_app()

    """
        测试卸载系统应用
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_uninstall_system_app(self):
        uninstall_app = UninstallApp(self.driver)
        uninstall_app.test_system_app_can_uninstall()

    """
        测试更新单个应用
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_update_one_app(self):
        update_app = UpdateApp(self.driver)
        update_app.test_update_one_app()

    """
        测试更新全部应用
    """
    # @unittest.skipIf(skip_case, skip_reason)
    def test_a_update_all_app(self):
        update_app = UpdateApp(self.driver)
        update_app.test_update_all_apps()







if __name__ == "__main__":

    Utils.Logging.error("纸飞机反击反击减肥减肥111")

    time.sleep(10)
    suiteAll = unittest.TestSuite()
    test1 = unittest.TestLoader().loadTestsFromTestCase(AppManageTest)
    # test2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    suiteAll.addTest(test1)
    runner = HtmlReport.get_generate_report_object()
    runner.run(suiteAll)

    # 发送邮件
    # start_send_email()

