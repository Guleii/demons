# coding:utf-8
__author__ = 'Alan'
'''
description: 应用市场 --》停止应用
'''

import random
import time
from general import Utils
from general.KeyCodeSentUtils import KeyCode
from src.common.moudle import LauncherUtils, LauncherBasePage
from moudle.LauncherBasePage import LauncherBasePage
from src.common.moudle.InputManagerUtils import InputManager
from general.ImageUtils import ImageUtil
from src.pages.appManage.AppManageDataConfig import *
from general.AdbUtils import ADB
from config import GlobalConfig as gl

class StopApp(LauncherBasePage):

    """
        定位到应用市场位置
    """
    def location_app_market(self):
        LauncherUtils.move_to_target_location(driver=self.driver,
                                              key_down_repeat_count=app_market_location["key_down_repeat_count"],
                                              key_down_wait_time=app_market_location["key_down_wait_time"],
                                              key_left_repeat_count=app_market_location["key_left_repeat_count"],
                                              key_left_wait_time=app_market_location["key_left_wait_time"],
                                              key_right_repeat_count=app_market_location["key_right_repeat_count"],
                                              key_right_wait_time=app_market_location["key_right_wait_time"],
                                              key_center_repeat_count=app_market_location["key_center_repeat_count"],
                                              key_center_wait_time=app_market_location["key_center_wait_time"],
                                              key_back_repeat_count=app_market_location["key_back_repeat_count"],
                                              key_back_wait_time=app_market_location["key_back_wait_time"],
                                              wait_time=app_market_location["wait_time"],
                                              tab_index=app_market_location["tab_index"],
                                              need_first_back=app_market_location["need_first_back"])

    """
         测试停止单个应用
     """
    def test_stop_app(self):
        self.location_app_market()

        self.check_has_stop_ps()

        self.reset_app()

    """
         检测是否正确停止应用进程
     """
    def check_has_stop_ps(self):
        while True:
            KeyCode.touch_down(self.driver)
            try:
                stop_button_index, stop_button_view_elements = self.find_need_stop_view_index()

                if stop_button_view_elements:
                    stop_button_view = stop_button_view_elements[
                        stop_button_index]  # 根据要停止的应用名称对应的index获取到对应的强行停止的view的index
                    stop_button_view.click()
                    self.check_ps_has_stop_ps()
                break
            except Exception:
                pass

    """
        找到需要停止的应用的"强行停止"按钮的index
    """
    def find_need_stop_view_index(self):
        self.check_has_element_by_text(stop_app_name)
        stop_button_view_elements = self.driver.find_elements_by_id(stop_app_view_id)  # 获取显示应用的强行停止的view集合
        stop_text_view_elements = self.driver.find_elements_by_id(stop_app_name_text_view_id)  # 获取显示应用的名称的view集合
        stop_button_index = 0
        if stop_text_view_elements:
            for view in stop_text_view_elements:
                index = stop_text_view_elements.index(view)
                text = view.text()
                if text == stop_app_name:
                    stop_button_index = index  # 找到要停止的应用名称对应的index
                    break
        return stop_button_index, stop_button_view_elements

    """
        获取当前正在运行的进程名称，判断里面是否包含已经停止的进程名称
    """
    def check_ps_has_stop_ps(self):
        ps_list = ADB(gl.test_app_more_device_device_name).get_ps()
        if stop_app_process_name in ps_list:
            raise Exception(stop_app_fail_message)

    """
        位置复位
    """
    def location_reset(self):
        KeyCode.touch_back(self.driver, repeat_count=app_manage_location_reset_back_count, wait_time=enter_manage_app_wait_time)

