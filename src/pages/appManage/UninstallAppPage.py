# coding:utf-8
__author__ = 'Alan'
'''
description: 应用市场 --》卸载应用
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


class SearchApp(LauncherBasePage):

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
         测试单个需要卸载的应用
     """
    def test_uninstall_app(self):
        self.location_app_market()
        self.location_one_uninstall_app()
        self.check_has_uninstall_app_successful()
        self.reset_app()

    """
        定位到单个需要卸载的应用
    """
    def location_one_uninstall_app(self):
        if self.check_has_update_app():
            KeyCode.touch_down(self.driver, repeat_count=2)
        KeyCode.touch_center(self.driver, wait_time=enter_manage_app_wait_time,
                             after_time=after_enter_manage_app_wait_time)

    """
        判断是否卸载应用成功
    """
    def check_has_uninstall_app_successful(self):
        app_name_element = self.driver.find_element_by_id(
            uninstall_app_view_app_name_resource_id)  # 获取卸载弹框的显示卸载应用名称的View
        uninstall_app_name = app_name_element.text()  # 获取卸载弹框的显示卸载应用的名称
        self.driver.find_element_by_id(unintall_app_view_recource_id)  # 判断是否弹出卸载框
        KeyCode.touch_center(self.driver, wait_time=enter_manage_app_wait_time,
                             after_time=after_enter_manage_app_wait_time)
        time.sleep(uninstall_later_wait_time)
        self.check_has_element_by_text(uninstall_app_name)

    """
        判断是否有可以更新的应用
    """
    def check_has_update_app(self):
        try:
            self.driver.find_element_by_id(update_all_view_resource_id)
            return True
        except Exception:
            return False

    """
        位置复位
    """
    def location_reset(self):
        KeyCode.touch_back(self.driver, repeat_count=app_manage_location_reset_back_count, wait_time=enter_manage_app_wait_time)

