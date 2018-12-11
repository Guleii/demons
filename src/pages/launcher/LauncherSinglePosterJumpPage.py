# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher 单张海报点击跳转测试
'''

from general.Base_page import Base
from moudle.HomeTabUtils import TabUtils
from moudle import HomeTabUtils

from general.KeyCodeSentUtils import *
from general import Utils as U


class SinglePosterJump(Base):
    # 爱奇艺-奇异果配置
    ai_qi_yi_package = 'com.gitvjimi.video'
    target_text = '首页'  # 跳转是否成功的比对值
    function_perform_time = 2  # 函数执行前需要等待的时间
    key_down_count = 1  # 需要按下遥控器的下键几次才能到达目标海报
    tab_index = HomeTabUtils.tab_two  # 目标海报位于那个Tab下
    key_back_wait_time = 2
    key_down_wait_time = 1
    key_center_wait_time = 3