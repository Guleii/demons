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


class UninstallApp(LauncherBasePage):

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
        uninstall_app_name = app_name_element.text  # 获取卸载弹框的显示卸载应用的名称
        self.driver.find_element_by_id(unintall_app_view_recource_id)  # 判断是否弹出卸载框
        KeyCode.touch_center(self.driver, wait_time=enter_manage_app_wait_time,
                             after_time=after_enter_manage_app_wait_time)
        time.sleep(uninstall_later_wait_time)
        try:
            self.check_has_element_by_text(uninstall_app_name)
            raise Exception(uninstall_app_fail)
        except Exception:
            pass

        time.sleep(uninstall_later_wait_time)

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
        检测系统应用的卸载应用按钮是否可以被选中
    """
    def test_system_app_can_uninstall(self):
        self.location_app_market()
        self.find_uninstall_button_and_check_attribute()
        self.location_reset()

    """
        找到卸载按钮并检查其属性
    """
    def find_uninstall_button_and_check_attribute(self):
        while True:
            KeyCode.touch_down(self.driver)
            try:
                self.check_has_element_by_text(uninstall_system_app_name)
                Utils.Logging.info("。。。。。。。。。。。。。。。。。。。找到电子说明书")
                uninstall_button_index, uninstall_button_view_elements = self.find_need_uninstall_system_view_index()
                Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始 找到对应多个元素  6666666666 ")
                time.sleep(uninstall_later_wait_time)

                Utils.Logging.info("。。。。。。。。。。。。。。。。。。。            开始检测系统属性")
                self.check_uninstall_button_attribute(uninstall_button_index, uninstall_button_view_elements)
                break
            except Exception:
                pass

    """
        检查卸载按钮的属性
    """
    def check_uninstall_button_attribute(self, uninstall_button_index, uninstall_button_view_elements):
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始检测系统应用的属性")
        if uninstall_button_view_elements:
            uninstall_system_app = uninstall_button_view_elements[
                uninstall_button_index]  # 根据要停止的应用名称对应的index获取到对应的强行停止的view的index
            Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始 找到系统应用的卸载应用的view")
            focusable = uninstall_system_app.get_attribute(uninstall_app_button_attribute)
            Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始 获取到 卸载应用对应属性： "+str(focusable))
            if focusable == uninstall_app_button_attribute_value:
                raise Exception(system_app_can_uninstall)

    """
         找到需要停止的应用的"强行停止"按钮的index
     """

    def find_need_uninstall_system_view_index(self):
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始 查找多个元素  1111111")
        uninstall_button_view_elements = self.driver.find_elements_by_id(uninstall_app_button_view_id)  # 获取显示应用的强行停止的view集合
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始 查找多个元素  222222222222 ")
        uninstall_text_view_elements = self.driver.find_elements_by_id(stop_app_name_text_view_id)  # 获取显示应用的名称的view集合
        uninstall_button_index = 0
        if uninstall_text_view_elements:
            for view in uninstall_text_view_elements:
                index = uninstall_text_view_elements.index(view)
                Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始 查找多个元素  3333 ")
                text = view.text
                if text == uninstall_system_app_name:
                    Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始 找到对应多个元素  44444444444 ")
                    uninstall_button_index = index  # 找到要停止的应用名称对应的index
                    Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始 找到对应多个元素  555555555555555 ")
                    break
        return uninstall_button_index, uninstall_button_view_elements

    """
        位置复位
    """
    def location_reset(self):
        KeyCode.touch_back(self.driver, repeat_count=app_manage_location_reset_back_count, wait_time=enter_manage_app_wait_time)

