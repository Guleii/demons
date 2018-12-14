# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher 多级海报点击跳转测试
'''

from general.Base_page import Base
from moudle.HomeTabUtils import TabUtils
from moudle import HomeTabUtils

from general.KeyCodeSentUtils import *


def move_to_target_location(driver, key_down_repeat_count=0, key_down_wait_time=1, key_left_repeat_count=0,
                            key_left_wait_time=1, key_right_repeat_count=0, key_right_wait_time=1, tab_index=1,
                            wait_time=2,
                            key_center_repeat_count=0, key_center_wait_time=0,
                            key_back_repeat_count=2,
                            key_back_wait_time=0,
                            need_first_back=True):
    time.sleep(wait_time)
    if need_first_back:
        KeyCode.touch_back(driver, wait_time=key_down_wait_time, repeat_count=key_back_repeat_count)
    if tab_index == HomeTabUtils.tab_two:
        TabUtils.click_tab_by_input_index(driver, HomeTabUtils.tab_eleven)
    else:
        TabUtils.click_tab_by_input_index(driver, HomeTabUtils.tab_one)
    time.sleep(wait_time)
    TabUtils.click_tab_by_input_index(driver, tab_index)

    KeyCode.touch_down(driver, wait_time=key_down_wait_time, repeat_count=key_down_repeat_count)
    KeyCode.touch_left(driver, wait_time=key_left_wait_time, repeat_count=key_left_repeat_count)
    KeyCode.touch_right(driver, wait_time=key_right_wait_time, repeat_count=key_right_repeat_count)
    KeyCode.touch_center(driver, wait_time=key_center_wait_time, repeat_count=key_center_repeat_count)