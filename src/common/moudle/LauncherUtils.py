# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher 多级海报点击跳转测试
'''

from general.Base_page import Base
from moudle.HomeTabUtils import TabUtils
from moudle import HomeTabUtils

from general.KeyCodeSentUtils import *


def move_to_target_location(driver, key_down_repeat_count, key_down_wait_time, key_left_repeat_count,
                            key_left_wait_time, key_right_repeat_count, key_right_wait_time, tab_index, wait_time):
    time.sleep(wait_time)
    TabUtils.click_tab_by_input_index(driver, tab_index)
    KeyCode.touch_down(driver, wait_time=key_down_wait_time, repeat_count=key_down_repeat_count)
    KeyCode.touch_left(driver, wait_time=key_left_wait_time, repeat_count=key_left_repeat_count)
    KeyCode.touch_right(driver, wait_time=key_right_wait_time, repeat_count=key_right_repeat_count)