# coding:utf-8
__author__ = 'machunyan'
'''
description: Launcher 稳定性测试逻辑类
'''

import random
import time
from general import Utils
from general.KeyCodeSentUtils import KeyCode
from src.common.moudle import LauncherUtils, LauncherBasePage
from src.common.moudle.InputManagerUtils import InputManager

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


class LauncherStability(LauncherBasePage):

    def click_switch_poster_up_down(self):

        for num in range(1, execNumber):

            Utils.Logging.debug("已执行次数：%i" % num)
            LauncherUtils.move_to_target_location(self.driver, key_down_repeat_count=20,
                                                  key_down_wait_time=3, tab_index=3)

    def click_search_more(self):
        count = 0
        for num in range(1, execNumber/2):

            # 随机生成一个键盘数，并点击搜索后的影视
            LauncherUtils.move_to_target_location(self.driver, key_down_repeat_count=1,
                                                  key_down_wait_time=3, tab_index=1)
            time.sleep(1)

            one = random.randint(1, len(listKeyBoard)-1)
            method_name = listKeyBoard[one]
            time.sleep(1)
            self.method_map(method_name)

            KeyCode.touch_right(self.driver, repeat_count=2, wait_time=1)
            KeyCode.touch_center(self.driver, wait_time=1)
            KeyCode.touch_back(self.driver, wait_time=1)
            count = count+1

            # 重新归位到tab搜索框， 否则后面的点击焦点会错乱
            LauncherUtils.move_to_target_location(self.driver, key_down_repeat_count=1,
                                                  key_down_wait_time=1, tab_index=1)

            # 再次生成一个随机键盘数， 两个字母搜索影视后点击， 并返回重新执行
            one = random.randint(1, len(listKeyBoard)-1)
            method_name = listKeyBoard[one]
            print(method_name)
            time.sleep(1)
            self.method_map(method_name)

            KeyCode.touch_right(self.driver, repeat_count=2, wait_time=1)
            KeyCode.touch_center(self.driver, wait_time=1)
            KeyCode.touch_back(self.driver, wait_time=1)
            InputManager.input_clear(self.driver, before_wait_time=1, after_wait_time=1)
            time.sleep(1)
            count = count + 1

            Utils.Logging.debug(method_name)
            Utils.Logging.debug("已搜索了%i次" % count)

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