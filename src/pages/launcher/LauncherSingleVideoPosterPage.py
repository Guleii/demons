# coding:utf-8
from general.ImageContrastUtils import ImageContrast

__author__ = 'Alan'
'''
description: Launcher 单张海报点击跳转测试
'''
from moudle.LauncherBasePage import LauncherBasePage
from general.Base_page import Base
from moudle.HomeTabUtils import TabUtils
from general.ImageUtils import ImageUtil
from moudle import HomeTabUtils
from moudle import LauncherUtils

from general.KeyCodeSentUtils import *
from general import Utils as U
from general.AdbUtils import ADB
from config import GlobalConfig as gl


class SingleVideoPoster(LauncherBasePage):
    first_screen_shot_name = "first_screen_shot"  # 第一张截图的默认名称
    second_screen_shot_name = "second_screen_shot"  # 第二张截图的默认名称
    perform_first_screen_shot_wait_time = 1    # 第一张截图执行前默认等待的时间
    perform_second_screen_shot_wait_time = 1   # 第二张截图执行前默认等待的时间
    image_contrast_percent = 10   # 图片默认对比是否一致的百分比
    picture_format = ".png"  # 图片格式
    screen_width = 1920  # 要测量的设备的宽
    screen_height = 1080  # 要测量的设备的高
    screen_shot_left_up_x = 0
    screen_shot_left_up_y = 0
    screen_shot_right_down_x = screen_width
    screen_shot_right_down_y = screen_height
    err_message = "第三方视频无法播放"  # 要测量的设备的高

    def check_video_has_playing_normal(self, perform_first_screen_shot_wait_time=perform_first_screen_shot_wait_time,
                                       perform_second_screen_shot_wait_time=perform_second_screen_shot_wait_time,
                                       first_screen_shot_name=first_screen_shot_name,
                                       second_screen_shot_name=second_screen_shot_name,
                                       image_contrast_percent=image_contrast_percent,
                                       screen_shot_left_up_x=screen_shot_left_up_x,
                                       screen_shot_left_up_y=screen_shot_left_up_y,
                                       screen_shot_right_down_x=screen_shot_right_down_x,
                                       screen_shot_right_down_y=screen_shot_right_down_y,
                                       err_message=err_message):
        ImageUtil.check_video_has_playing_normal(self.driver,
                                                 perform_first_screen_shot_wait_time=perform_first_screen_shot_wait_time,
                                                 perform_second_screen_shot_wait_time=perform_second_screen_shot_wait_time,
                                                 first_screen_shot_name=first_screen_shot_name,
                                                 second_screen_shot_name=second_screen_shot_name,
                                                 image_contrast_percent=image_contrast_percent,
                                                 screen_shot_left_up_x=screen_shot_left_up_x,
                                                 screen_shot_left_up_y=screen_shot_left_up_y,
                                                 screen_shot_right_down_x=screen_shot_right_down_x,
                                                 screen_shot_right_down_y=screen_shot_right_down_y,
                                                 err_message=err_message)




