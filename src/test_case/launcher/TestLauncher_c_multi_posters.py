# -*- coding: utf-8 -*-

"""HTMLTestRunner 截图版示例 appium版"""
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
                Launcher:多级海报点击测试
    """
    # @unittest.skipIf(skip_case, skip_reason)
    def test_b_b_launcher_multi_posters_jump(self):
        multi_posters = MultiPosters(self.driver)
        multi_posters.click_multi_posters_to_detail_no_config(tab_index=multi_posters.tab_six,
                                                              key_down_repeat_count=2, key_left_repeat_count=1,
                                                              key_right_repeat_count=2, target_text='贝瓦儿歌',
                                                              key_center_wait_time=5)
        # multi_posters.click_multi_posters_to_detail_no_config(tab_index=HomeTabUtils.tab_two,
        #                                                       key_down_repeat_count=1, key_left_repeat_count=0,
        #                                                       key_right_repeat_count=0,
        #                                                       key_center_wait_time=3)







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



