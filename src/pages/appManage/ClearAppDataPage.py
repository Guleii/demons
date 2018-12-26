# coding:utf-8
import traceback

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


class ClearAppData(LauncherBasePage):

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
         测试需要清除数据的应用
     """
    def test_clear_app_data(self):
        self.location_app_market()

        self.clear_app_data()

        self.check_app_data_has_cleared()

        self.reset_app()

    """
        检测指定app的数据是否清除
    """
    def check_app_data_has_cleared(self):
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始  检测指定app的数据是否清除")
        KeyCode.touch_back(self.driver, repeat_count=app_manage_location_reset_back_count)
        time.sleep(enter_manage_app_wait_time)
        LauncherUtils.open_launcher_app_tab_app(self.driver, app_name=clear_data_test_app_name,
                                                tab_index=HomeTabUtils.tab_eleven)
        time.sleep(enter_app_later_wait_time)
        try:
            Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始  查找权限矿的允许元素： ")
            self.driver.find_element_by_id(permission_dialog_allow_button_resource_id)
        except Exception:
            raise Exception(clear_app_data_fail + "-" + clear_data_test_app_name)
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始  按下home键")
        KeyCode.touch_home(self.driver)

    """
        清除指定app的数据
    """
    def clear_app_data(self):
        while True:
            KeyCode.touch_down(self.driver)
            try:
                Utils.Logging.info("。。。。。。。。。。。。。。。。。。。查找指定清除的元素")
                clear_button_index, clear_button_view_elements = self.find_need_clear_view_index()
                Utils.Logging.info("。。。。。。。。。。。。。。。。。。。找到多个元素")
                if clear_button_view_elements:
                    Utils.Logging.info("。。。。。。。。。。。。。。。。。。。;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;找到了指定清除的元素")
                    clear_button_view = clear_button_view_elements[clear_button_index]  # 根据要停止的应用名称对应的index获取到对应的清除数据的view的index
                    time.sleep(enter_app_later_wait_time)
                    Utils.Logging.info("。。。。。。。。。。。。。。。。。。。点击指定清除的元素 ，下标为： "+str(clear_button_index))
                    clear_button_view.click()
                    break

            except Exception:

                # Utils.Logging.info("。。。。。。。。。。。。。。。。。。。查找元素异常： " +  str(traceback.print_exc()))
                pass

    """
           找到需要清除数据的应用的"清除数据"按钮的index
    """
    def find_need_clear_view_index(self):
        # time.sleep(enter_app_later_wait_time)
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。开始查找指定多个元素 1111111111111111111111111111")
        self.check_has_element_by_text(text=clear_data_test_app_name)
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。多个元素找到 wps22222222222222222222222222222 ")
        clear_button_view_elements = self.driver.find_elements_by_id(clear_data_view_id)  # 获取显示应用的清除数据的view集合
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。开始找多个元素的集合wps 3333333333333333333333333333333333333333")
        show_app_name_text_view_elements = self.driver.find_elements_by_id(stop_app_name_text_view_id)  # 获取显示应用的名称的view集合
        clear_button_index = 0
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。查找指定多个元素")
        if show_app_name_text_view_elements:
            for view in show_app_name_text_view_elements:
                Utils.Logging.info("。。。。。。。。。。。。。。。。。。。查找指定多个元素 1111： ")
                index = show_app_name_text_view_elements.index(view)
                Utils.Logging.info("。。。。。。。。。。。。。。。。。。。查找指定多个元素 2222222： " )
                text = view.text   #  一定不要写成text()不然会报错
                Utils.Logging.info("。。。。。。。。。。。。。。。。。。。查找指定多个元素 333333333： "+text)
                if text == clear_data_test_app_name:
                    clear_button_index = index  # 找到要停止的应用名称对应的index
                    Utils.Logging.info("。。。。。。。。。。。。。。。。。。。找到指定 文本： " + text)
                    break
        return clear_button_index, clear_button_view_elements

    """
        位置复位
    """
    def location_reset(self):
        KeyCode.touch_back(self.driver, repeat_count=app_manage_location_reset_back_count, wait_time=enter_manage_app_wait_time)

