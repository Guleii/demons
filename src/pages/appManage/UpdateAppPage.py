# coding:utf-8
__author__ = 'Alan'
'''
description: 应用市场 --》搜索应用
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
        定位到单个应用更新
    """
    def location_one_app_update(self):
        KeyCode.touch_down(self.driver)
        KeyCode.touch_center(self.driver, wait_time=enter_manage_app_wait_time,
                             after_time=after_enter_manage_app_wait_time)

    """
        判断是否有可以更新的应用
    """
    def check_has_update_app(self):
        try:
            return self.driver.find_element_by_id(update_all_view_resource_id)
        except Exception:
            raise Exception(no_need_update_apps)

    """
        检测全部应用更新
    """
    def test_update_all_apps(self):
        self.location_app_market()
        update_element = self.check_has_update_app()
        update_element.click()
        check_count = 0
        self.check_update_all_is_successful(check_count)
        self.location_reset()

    """
        检测单个应用更新
    """
    def test_update_one_app(self):
        self.location_app_market()
        self.check_has_update_app()
        num_view = self.driver.find_element_by_id(update_all_number_view_resource_id)
        update_before_need_update_app_num = num_view.text()  # 获取可以更新应用数量

        self.location_one_app_update()

        self.check_update_one_app_is_successful(update_before_need_update_app_num)

        self.location_reset()

    """
        检测单个应用更新是否成功
    """
    def check_update_one_app_is_successful(self, update_before_need_update_app_num):
        check_count = 0
        while True:
            time.sleep(check_update_all_app_wait_time)
            check_count += 1
            KeyCode.touch_back(self.driver)
            KeyCode.touch_center(self.driver, wait_time=enter_manage_app_wait_time,
                                 after_time=after_enter_manage_app_wait_time)
            num_view = self.driver.find_element_by_id(update_all_number_view_resource_id)
            update_after_need_update_app_num = num_view.text()  # 获取更新单个应用后可以更新应用数量
            if check_count > check_update_all_app_count:
                if update_before_need_update_app_num == update_after_need_update_app_num:
                    raise Exception(update_all_app_fail)
                else:
                    break
            else:
                if update_before_need_update_app_num != update_after_need_update_app_num:
                    break

    """
        检测应用更新是否全部成功
    """
    def check_update_all_is_successful(self, check_count):
        while True:
            time.sleep(check_update_all_app_wait_time)
            check_count += 1
            KeyCode.touch_back(self.driver)
            KeyCode.touch_center(self.driver, wait_time=enter_manage_app_wait_time,
                                 after_time=after_enter_manage_app_wait_time)

            if check_count > check_update_all_app_count:
                try:
                    self.driver.find_element_by_id(update_all_view_resource_id)
                    raise Exception(update_all_app_fail)
                except Exception:
                    break
            else:
                try:
                    self.driver.find_element_by_id(update_all_view_resource_id)
                except Exception:
                    break

    """
        位置复位
    """
    def location_reset(self):
        KeyCode.touch_back(self.driver, repeat_count=app_manage_location_reset_back_count, wait_time=enter_manage_app_wait_time)

