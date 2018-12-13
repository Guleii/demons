# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher 多级海报点击跳转测试
'''


from moudle import HomeTabUtils
from moudle.LauncherBasePage import LauncherBasePage

from general.KeyCodeSentUtils import *


class MultiPosters(LauncherBasePage):
    """
               点击多级海报跳转，
               wait_time = 函数执行前等待的时间
               target_text = '腾讯专区'  # 跳转是否成功的比对值
               function_perform_time = 2  # 函数执行前需要等待的时间
               key_down_count = 1  # 需要按下遥控器的下键几次才能到达目标海报
               tab_index = HomeTabUtils.tab_two  # 目标海报位于那个Tab下
               key_back_wait_time = 2 执行返回键前需要等待的时间
               key_down_wait_time = 1
               key_center_wait_time = 3
               key_back_repeat_count = 1 向下按键需要重复执行几次
       """

    def click_multi_posters_to_detail_no_config(self, wait_time=LauncherBasePage.function_perform_time,
                                                tab_index=HomeTabUtils.tab_one, target_text=LauncherBasePage.target_text,
                                                key_down_wait_time=LauncherBasePage.key_down_wait_time,
                                                key_down_repeat_count=LauncherBasePage.key_down_repeat_count,
                                                key_left_wait_time=LauncherBasePage.key_left_wait_time,
                                                key_left_repeat_count=LauncherBasePage.key_left_repeat_count,
                                                key_right_wait_time=LauncherBasePage.key_right_wait_time,
                                                key_right_repeat_count=LauncherBasePage.key_right_repeat_count,
                                                key_back_wait_time=LauncherBasePage.key_back_wait_time,
                                                key_center_wait_time=LauncherBasePage.key_center_wait_time,
                                                key_back_repeat_count=LauncherBasePage.key_back_repeat_count):
        self.move_to_target(key_down_repeat_count=key_down_repeat_count,
                            key_down_wait_time=key_down_wait_time,
                            key_left_repeat_count=key_left_repeat_count,
                            key_left_wait_time=key_left_wait_time,
                            key_right_repeat_count=key_right_repeat_count,
                            key_right_wait_time=key_right_wait_time,
                            tab_index=tab_index,
                            wait_time=wait_time)
        KeyCode.touch_center(self.driver, after_time=key_center_wait_time)
        self.check_has_element_by_text(text=target_text)
        KeyCode.touch_back(self.driver, wait_time=key_back_wait_time, repeat_count=key_back_repeat_count)
        self.touch_back(key_back_repeat_count=1)



