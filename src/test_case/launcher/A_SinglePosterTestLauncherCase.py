# -*- coding: utf-8 -*-
# coding:utf-8

__author__ = 'Alan'
'''
description: Launcher 单张海报点击跳转测试
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

skip_case = True
skip_reason = "调试"


class LauncherTest(BaseUnittest.BaseTestCase):

    """
        判断点击海报是否正确的播放视频以及返回复位
    """
    def check_video_jump_is_right_and_back(self):
        single_video_poster = SingleVideoPoster(self.driver)
        single_video_poster.check_video_has_playing_normal()
        single_video_poster.touch_back(key_back_repeat_count=3,key_back_wait_time=1)

    """
        单张海报跳转到聚体育  点击海报正确的播放视频
    """
    # @unittest.skipIf(skip_case, skip_reason)
    def test_a_a_ju_ti_yu_poster(self):
        LauncherUtils.move_to_target_location(driver=self.driver, tab_index=HomeTabUtils.tab_nine,
                                              key_down_repeat_count=1, key_left_repeat_count=0,
                                              key_right_repeat_count=0, key_center_repeat_count=1,
                                              )
        # self.check_video_jump_is_right_and_back()

    """
        单张海报跳转到芒果TV 点击海报正确的播放视频
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_b_mang_guo_poster(self):
        LauncherUtils.move_to_target_location(driver=self.driver, tab_index=HomeTabUtils.tab_eight,
                                              key_down_repeat_count=1, key_left_repeat_count=0,
                                              key_right_repeat_count=0, key_center_repeat_count=1)
        self.check_video_jump_is_right_and_back()

    """
        单张海报跳转到爱奇艺  点击海报正确的播放视频
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_a_c_ai_qi_yi_poster(self):
        LauncherUtils.move_to_target_location(driver=self.driver, tab_index=HomeTabUtils.tab_five,
                                              key_down_repeat_count=1, key_left_repeat_count=0,
                                              key_right_repeat_count=0, key_center_repeat_count=1)
        self.check_video_jump_is_right_and_back()




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

