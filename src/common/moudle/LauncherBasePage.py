# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher 的basePage
'''
from general.Base_page import Base
from moudle import LauncherUtils
from moudle import HomeTabUtils
from moudle import HomeTabUtils


class LauncherBasePage(Base):

    # 分别对应Launcher的Tab_index
    tab_one = HomeTabUtils.tab_one
    tab_two = HomeTabUtils.tab_two
    tab_three = HomeTabUtils.tab_three
    tab_four = HomeTabUtils.tab_four
    tab_five = HomeTabUtils.tab_five
    tab_six = HomeTabUtils.tab_six
    tab_seven = HomeTabUtils.tab_seven
    tab_eight = HomeTabUtils.tab_eight
    tab_nine = HomeTabUtils.tab_nine
    tab_ten = HomeTabUtils.tab_ten
    tab_eleven = HomeTabUtils.tab_eleven

    target_text = '腾讯专区'  # 跳转是否成功的比对值
    function_perform_time = 2  # 函数执行前需要等待的时间
    key_down_count = 1  # 需要按下遥控器的下键几次才能到达目标海报
    tab_index = HomeTabUtils.tab_two  # 目标海报位于那个Tab下
    key_back_wait_time = 2
    key_back_repeat_count = 1
    key_down_wait_time = 1
    key_down_repeat_count = 1
    key_left_wait_time = 2
    key_left_repeat_count = 1
    key_right_wait_time = 2
    key_right_repeat_count = 1
    key_center_wait_time = 3
    key_center_repeat_count = 2

    def move_to_target(self, key_down_repeat_count=key_down_repeat_count,
                       key_down_wait_time=key_down_wait_time,
                       key_left_repeat_count=key_left_repeat_count,
                       key_left_wait_time=key_left_wait_time,
                       key_right_repeat_count=key_right_repeat_count,
                       key_right_wait_time=key_right_wait_time,
                       tab_index=tab_index,
                       wait_time=function_perform_time):
        LauncherUtils.move_to_target_location(driver=self.driver,
                                              key_down_repeat_count=key_down_repeat_count,
                                              key_down_wait_time=key_down_wait_time,
                                              key_left_repeat_count=key_left_repeat_count,
                                              key_left_wait_time=key_left_wait_time,
                                              key_right_repeat_count=key_right_repeat_count,
                                              key_right_wait_time=key_right_wait_time,
                                              tab_index=tab_index,
                                              wait_time=wait_time)
