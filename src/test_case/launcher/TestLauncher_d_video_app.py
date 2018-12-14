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
            Launcher:点击任意一个非内置应用海报，判断是否下载成功 云视听极光
        """

    @unittest.skipIf(skip_case, skip_reason)
    def test_c_a_launcher_app_load_yun_shi_ting_ji_guang(self):
        single_poster = SingleAppPosterJump(self.driver)
        single_poster.test_load_or_enter_video_app(app_package=single_poster.yun_shi_ting_ji_guang,
                                                   key_down_repeat_count=7, tab_index=single_poster.tab_two)
        single_poster.touch_back(key_back_repeat_count=2)

    """
        Launcher:点击任意一个非内置应用海报，判断是否下载成功     CIBN酷喵影视
    """

    @unittest.skipIf(skip_case, skip_reason)
    def test_c_b_launcher_app_load_cibn_ku_miao_ying_shi(self):
        KeyCode.touch_left(self.driver)
        single_poster = SingleAppPosterJump(self.driver)
        single_poster.test_load_or_enter_video_app(app_package=single_poster.cibn_ku_miao_ying_shi,
                                                   key_down_repeat_count=7, key_right_repeat_count=2,
                                                   tab_index=single_poster.tab_two)
        single_poster.touch_back(key_back_repeat_count=2)

    """
        Launcher:点击任意一个非内置应用海报，判断是否下载成功  yun_shi_ting_mao   云视听电视猫
    """

    # @unittest.skipIf(skip_case, skip_reason)
    def test_c_c_launcher_app_load_yun_shi_ting_mao(self):
        single_poster = SingleAppPosterJump(self.driver)
        single_poster.test_load_or_enter_video_app(app_package=single_poster.yun_shi_ting_dian_shi_mao,
                                                   key_down_repeat_count=7, key_right_repeat_count=4,
                                                   tab_index=single_poster.tab_two)

    """
         Launcher:点击任意一个非内置应用海报，判断是否下载成功    哔哩哔哩TV版
    """

    # @unittest.skipIf(skip_case, skip_reason)
    def test_c_d_launcher_app_load_bili_bili(self):
        # 哔哩哔哩
        single_poster = SingleAppPosterJump(self.driver)
        LauncherUtils.move_to_target_location(driver=self.driver, tab_index=HomeTabUtils.tab_two,
                                              key_down_repeat_count=1, key_right_repeat_count=2,
                                              key_center_repeat_count=1, key_back_repeat_count=2)
        single_poster.test_load_or_enter_video_app(app_package=single_poster.bi_li_bi_li_tv, key_down_repeat_count=1,
                                                   tab_index=single_poster.tab_two, key_back_repeat_count=0,
                                                   need_first_back=False)

    """
        Launcher:点击任意一个非内置应用海报，判断是否下载成功   FitTime
    """

    @unittest.skipIf(skip_case, skip_reason)
    def test_c_e_launcher_app_load_fit_time(self):
        single_poster = SingleAppPosterJump(self.driver)
        LauncherUtils.move_to_target_location(driver=self.driver, tab_index=HomeTabUtils.tab_eleven,
                                              key_down_repeat_count=1, key_right_repeat_count=2,
                                              key_center_repeat_count=1, key_back_repeat_count=2)
        single_poster.test_load_or_enter_video_app(app_package=single_poster.fit_time, key_down_repeat_count=1,
                                                   tab_index=single_poster.tab_two, key_back_repeat_count=0,
                                                   need_first_back=False)
        time.sleep(15)

    """
        Launcher:点击任意一个非内置应用海报，判断是否下载成功   百视通TV
    """

    @unittest.skipIf(skip_case, skip_reason)
    def test_c_f_launcher_app_load_fit_time(self):
        single_poster = SingleAppPosterJump(self.driver)
        LauncherUtils.move_to_target_location(driver=self.driver, tab_index=HomeTabUtils.tab_seven,
                                              key_down_repeat_count=2, key_right_repeat_count=2,
                                              key_center_repeat_count=1, key_back_repeat_count=0)
        single_poster.test_load_or_enter_video_app(app_package=single_poster.bai_shi_tong_tv, key_down_repeat_count=3,
                                                   tab_index=single_poster.tab_two, key_back_repeat_count=0,
                                                   need_first_back=False)



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



