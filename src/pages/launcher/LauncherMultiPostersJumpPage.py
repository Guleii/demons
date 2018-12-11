# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher 多级海报点击跳转测试
'''

from general.Base_page import Base
from moudle.HomeTabUtils import TabUtils
from moudle import HomeTabUtils

from general.KeyCodeSentUtils import *
from general import Utils as U


class MultiPosters(Base):
    target_text = '腾讯专区'  # 跳转是否成功的比对值
    function_perform_time = 2  # 函数执行前需要等待的时间
    key_down_count = 1  # 需要按下遥控器的下键几次才能到达目标海报
    tab_index = HomeTabUtils.tab_two  # 目标海报位于那个Tab下
    key_back_wait_time = 2
    key_down_wait_time = 1
    key_center_wait_time = 3
    key_center_repeat_count = 2

    """
        从Tab栏的左边往右点击，
        wait_time = 函数执行前等待的时间
    """
    def click_multi_posters_to_detail(self, wait_time=function_perform_time):
        time.sleep(wait_time)
        TabUtils.click_tab_by_input_index(self.driver, self.tab_index)
        KeyCode.touch_down(self.driver, wait_time=self.key_down_wait_time)
        KeyCode.touch_center(self.driver, after_time=self.key_center_wait_time)
        self.check_has_element_by_text(text=self.target_text)
        KeyCode.touch_back(self.driver, wait_time=self.key_back_wait_time, repeat_count=self.key_center_repeat_count)


