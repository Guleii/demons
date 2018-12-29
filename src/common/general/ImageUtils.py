# coding:utf-8
__author__ = 'Alan'
'''
description: 图片对比工具类
'''
import time
from general.ImageContrastUtils import ImageContrast
from config import GlobalConfig as gl
from general.KeyCodeSentUtils import KeyCode
from general.more_devices.BaseAndroidPhone import *
from general import FileUtils

can_get_device_screen_size = "无法获取屏幕分辨率"


class ImageUtil:
    first_screen_shot_name = gl.test_app_more_device_device_identity_prefix + "first_screen_shot"  # 第一张截图的默认名称
    second_screen_shot_name = gl.test_app_more_device_device_identity_prefix + "second_screen_shot"  # 第二张截图的默认名称
    perform_first_screen_shot_wait_time = 10  # 第一张截图执行前默认等待的时间
    perform_second_screen_shot_wait_time = 10  # 第二张截图执行前默认等待的时间
    image_contrast_percent = 10  # 图片默认对比是否一致的百分比
    picture_format = ".png"  # 图片格式
    screen_width = 1920  # 要测量的设备的宽
    screen_height = 1080  # 要测量的设备的高
    screen_shot_left_up_x = 0
    screen_shot_left_up_y = 0
    screen_shot_right_down_x_value = screen_width
    screen_shot_right_down_y_value = screen_height
    err_message = "第三方视频无法播放"  # 要测量的设备的高

    @staticmethod
    def check_video_has_playing_normal(driver, perform_first_screen_shot_wait_time=perform_first_screen_shot_wait_time,
                                       perform_second_screen_shot_wait_time=perform_second_screen_shot_wait_time,
                                       first_screen_shot_name=first_screen_shot_name,
                                       second_screen_shot_name=second_screen_shot_name,
                                       image_contrast_percent=image_contrast_percent,
                                       screen_shot_left_up_x=screen_shot_left_up_x,
                                       screen_shot_left_up_y=screen_shot_left_up_y,
                                       screen_shot_right_down_x=screen_shot_right_down_x_value,
                                       screen_shot_right_down_y=screen_shot_right_down_y_value,
                                       err_message=err_message, need_enter_center=False,
                                       key_center_repeat_count=1, key_center_wait_time=0):
        image_contrast = ImageContrast(driver)

        time.sleep(perform_first_screen_shot_wait_time)
        print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。开始拍第一张照片")
        image_contrast.get_screen_shot_by_custom_size(screen_shot_left_up_x, screen_shot_left_up_y,
                                                      screen_shot_right_down_x, screen_shot_right_down_y).write_to_file(gl.screen_shot_path, gl.test_app_more_device_device_identity_prefix + first_screen_shot_name)

        if need_enter_center:  # 是否需要进入
            print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。打开应用")
            KeyCode.touch_center(driver, repeat_count=key_center_repeat_count, wait_time=key_center_wait_time)

        time.sleep(perform_second_screen_shot_wait_time)
        image_contrast.get_screen_shot_by_custom_size(screen_shot_left_up_x, screen_shot_left_up_y,
                                                      screen_shot_right_down_x, screen_shot_right_down_y).write_to_file(gl.screen_shot_path, gl.test_app_more_device_device_identity_prefix + second_screen_shot_name)
        # result = imageContrast.get_screen_shot_by_element(element)
        mode_image = gl.screen_shot_path + gl.test_app_more_device_device_identity_prefix + first_screen_shot_name + gl.screen_shot_picture_format
        now_image = gl.screen_shot_path + gl.test_app_more_device_device_identity_prefix + second_screen_shot_name + gl.screen_shot_picture_format


        print(
            "...................................................  qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee   " + gl.test_app_more_device_device_identity_prefix + "   " + "  mac地址：    ")
        return image_contrast.same_as(mode_image, now_image, image_contrast_percent, err_message=err_message)


    """
        根据坐标截图截图
        返回图片地址
    """
    @staticmethod
    def screen_shot_by_location(driver, src_path=None, src_name=None, wait_time=2,
                                screen_shot_left_up_x=screen_shot_left_up_x,
                                screen_shot_left_up_y=screen_shot_left_up_y,
                                screen_shot_right_down_x=screen_shot_right_down_x_value,
                                screen_shot_right_down_y=screen_shot_right_down_y_value):
        image_contrast = ImageContrast(driver)

        time.sleep(wait_time)
        path = gl.screen_shot_path
        if src_path:
            path = src_path
            FileUtils.make_dir(path)
        image_contrast.get_screen_shot_by_custom_size(screen_shot_left_up_x, screen_shot_left_up_y,
                                                      screen_shot_right_down_x, screen_shot_right_down_y).write_to_file(
            path, gl.test_app_more_device_device_identity_prefix + src_name)
        return path+gl.test_app_more_device_device_identity_prefix + src_name

    """
        根据Element截图截图
           返回图片地址
    """
    @staticmethod
    def screen_shot_by_element(driver, element, src_path=None, src_name=None, wait_time=2,):
        image_contrast = ImageContrast(driver)
        time.sleep(wait_time)
        path = gl.screen_shot_path
        if src_path:
            path = src_path
            FileUtils.make_dir(path)

        image_contrast.get_screen_shot_by_element(element).write_to_file(
            path, gl.test_app_more_device_device_identity_prefix + src_name)
        return path + gl.test_app_more_device_device_identity_prefix + src_name

    """
        初始化默认屏幕分辨率
    """
    @staticmethod
    def choose_location_by_device_screen_size(screen_size=None):
        global screen_shot_right_down_x_value
        global screen_shot_right_down_y_value
        if len(screen_size) == 2:
            screen_shot_right_down_x_value = screen_size[0]
            screen_shot_right_down_y_value = screen_size[1]
        else:
            raise Exception(can_get_device_screen_size)


