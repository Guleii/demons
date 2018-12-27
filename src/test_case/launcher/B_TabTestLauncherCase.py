# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher Tab切换测试
'''
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

skip_case = False
skip_reason = "调试"


class LauncherTest(BaseUnittest.BaseTestCase):



    """
            Launcher:tab测试
    """
    # @unittest.skipIf(skip_case, skip_reason)
    def test_b_a_launcher_tab(self):
        KeyCodeSentUtils.KeyCode.touch_back(self.driver, 4)
        launcher_tab = LauncherTab(self.driver)
        launcher_tab.click_tab_from_left_to_right()





if __name__ == "__main__":

    Utils.Logging.error("纸飞机反击反击减肥减肥111")

    time.sleep(10)
    suiteAll = unittest.TestSuite()
    test1 = unittest.TestLoader().loadTestsFromTestCase(LauncherTest)
    # test2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    suiteAll.addTest(test1)
    runner = HtmlReport.get_generate_report_object()
    runner.run(suiteAll)

    # 发送邮件
    # start_send_email()



