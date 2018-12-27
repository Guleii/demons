# coding:utf-8
import unittest
from general import BaseUnittest
from general.HtmlReportUtils import HtmlReport
import random
import time
from general import Utils
from general.KeyCodeSentUtils import KeyCode
from moudle.HomeTabUtils import TabUtils
from src.common.moudle import LauncherUtils
from src.common.moudle.InputManagerUtils import InputManager

__author__ = 'machunyan'
'''
description: Launcher 稳定性测试用例类
'''

skip_case = False
skip_reason = "调试"
# 执行操作的次数
execNumber = 100

"""
定义的搜索键盘列表
"""
listKeyBoard = ['input_a', 'input_b', 'input_c', 'input_d', 'input_e',
                'input_f', 'input_g', 'input_h', 'input_i', 'input_j',
                'input_k', 'input_l', 'input_m', 'input_n', 'input_o',
                'input_p', 'input_q', 'input_r', 'input_s', 'input_t',
                'input_u', 'input_v', 'input_w', 'input_x', 'input_y',
                'input_z']


class LauncherStability(BaseUnittest.BaseTestCase):

    """
    在我的tab上下移动焦点
    """
    @unittest.skipIf(skip_case, skip_reason)
    def test_switch_poster_up_down(self):
        for num in range(1, execNumber):

            Utils.Logging.debug("已执行次数：%i" % num)
            LauncherUtils.move_to_target_location(self.driver, key_down_repeat_count=20,
                                                  key_down_wait_time=3, tab_index=2)

    @unittest.skipIf(skip_case, skip_reason)
    def test_search_more(self):
        time.sleep(4)
        count = 0
        for num in range(1, execNumber):
            KeyCode.touch_back(driver=self.driver, repeat_count=4)
            time.sleep(2)
            # 随机生成一个键盘数，并点击搜索后的影视
            KeyCode.touch_left(driver=self.driver)
            # LauncherUtils.move_to_target_location(self.driver, key_down_repeat_count=2, wait_time=5,
            #                                       key_down_wait_time=3, tab_index=1)
            time.sleep(2)

            # 搜索完键盘后，默认回到了搜索tab
            one = random.randint(1, len(listKeyBoard)-1)
            method_name = listKeyBoard[one]
            self.method_map(method_name)
            Utils.Logging.debug(method_name)
            time.sleep(2)
            # 因此需要先向下移动一位，后向右移动两位，并点击海报
            KeyCode.touch_down(self.driver, repeat_count=1, wait_time=3)
            KeyCode.touch_right(self.driver, repeat_count=2, wait_time=3)
            KeyCode.touch_center(self.driver, wait_time=3)
            KeyCode.touch_back(self.driver, wait_time=3)
            count = count+1
            time.sleep(3)
            InputManager.input_clear(self.driver, before_wait_time=1, after_wait_time=3)
            Utils.Logging.debug("已搜索了%i次" % count)

            """
            # 再次生成一个随机键盘数， 两个字母搜索影视后点击， 并返回重新执行
            one = random.randint(1, len(listKeyBoard)-1)
            method_name = listKeyBoard[one]
            Utils.Logging.debug(method_name)
            time.sleep(1)
            self.method_map(method_name)

            KeyCode.touch_right(self.driver, repeat_count=0, wait_time=1)
            KeyCode.touch_center(self.driver, wait_time=1)
            KeyCode.touch_back(self.driver, wait_time=1)
            InputManager.input_clear(self.driver, before_wait_time=1, after_wait_time=1)
            time.sleep(1)
            count = count + 1

            Utils.Logging.debug(method_name)
            Utils.Logging.debug("已搜索了%i次" % count)
            """

    def method_map(self, methd_name='input_five'):

        if methd_name == 'input_delete':
            InputManager.input_delete(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_clear':
            InputManager.input_clear(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_zero':
            InputManager.input_zero(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_one':
            InputManager.input_one(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_two':
            InputManager.input_three(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_three':
            InputManager.input_three(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_four':
            InputManager.input_four(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_five':
            InputManager.input_five(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_six':
            InputManager.input_six(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_seven':
            InputManager.input_seven(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_eight':
            InputManager.input_eight(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_nine':
            InputManager.input_nine(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_a':
            InputManager.input_a(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_b':
            InputManager.input_b(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_c':
            InputManager.input_c(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_d':
            InputManager.input_d(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_e':
            InputManager.input_e(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_f':
            InputManager.input_f(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_g':
            InputManager.input_g(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_h':
            InputManager.input_h(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_i':
            InputManager.input_i(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_j':
            InputManager.input_j(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_k':
            InputManager.input_k(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_l':
            InputManager.input_l(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_m':
            InputManager.input_m(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_n':
            InputManager.input_n(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_o':
            InputManager.input_o(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_p':
            InputManager.input_p(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_q':
            InputManager.input_q(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_r':
            InputManager.input_r(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_s':
            InputManager.input_s(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_t':
            InputManager.input_t(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_u':
            InputManager.input_u(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_v':
            InputManager.input_v(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_w':
            InputManager.input_w(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_w':
            InputManager.input_w(self.driver, after_wait_time=2, before_wait_time=2)
        elif methd_name == 'input_y':
            InputManager.input_y(self.driver, after_wait_time=2, before_wait_time=2)
        else:
            InputManager.input_five(self.driver, after_wait_time=2, before_wait_time=2)

    # def test_input(self):
    #     KeyCode.touch_back(driver=self.driver, repeat_count=4)
    #     time.sleep(2)
    #     # 随机生成一个键盘数，并点击搜索后的影视
    #     KeyCode.touch_left(driver=self.driver)
    #     time.sleep(3)
    #     # InputManager.input_three(self.driver)
    #     #InputManager.input_i(self.driver)
    #     # self.driver.tap([(168, 322), (240, 379)], 100)
    #     # self.driver.tap([(269, 236), (341, 293)], 100)
    #     self.driver.tap([(67, 322), (139, 379)], 100)
    #     time.sleep(3)
    #     # InputManager.find_text_view_by_text(self.driver, 'K').click()
    #     # time.sleep(3)
    #
    #     # InputManager.input_d(self.driver)
    #
    #     # InputManager.find_text_view_by_text(self.driver,'如需搜索：“极米”' )


if __name__ == '__main__':

    Utils.Logging.debug("Launcher稳定性测试")

    time.sleep(10)
    suteAll = unittest.TestSuite()
    test = unittest.TestLoader().loadTestsFromTestCase(LauncherStability)
    suteAll.addTest(test)
    runner = HtmlReport.get_generate_report_object()
    runner.run(suteAll)


