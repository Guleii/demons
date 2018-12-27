# coding:utf-8
__author__ = 'Alan'
'''
description: 应用市场 --》搜索应用测试
'''

import random
import time
from general import Utils
from general.KeyCodeSentUtils import KeyCode
from src.common.moudle import LauncherUtils, LauncherBasePage
from moudle.LauncherBasePage import LauncherBasePage
from src.common.moudle.InputManagerUtils import InputManager
from general.ImageUtils import ImageUtil
from general.AdbUtils import ADB
from config import GlobalConfig as gl
from src.pages.appMarket.AppMarketDataConfig import *


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
        定位到搜索接口的位置
    """
    def location_search_and_enter(self):
        KeyCode.touch_up(self.driver)
        KeyCode.touch_center(self.driver, after_time=enter_search_app_wait_time)

    """
        测试搜索应用是否成功
    """
    def start_test_search_app(self):
        time.sleep(enter_search_app_wait_time)
        self.remove_app_first()
        self.location_app_market()
        time.sleep(enter_search_app_wait_time)
        self.location_search_and_enter()
        self.enter_test_content()
        self.check_search_is_successful()
        self.check_search_result_can_use()

        self.location_reset()

    """
        测试前移除需要测试的应用
    """
    def remove_app_first(self):
        try:
            ADB(gl.test_app_more_device_device_name).remove_app(packageName=check_open_app_package_name)
            time.sleep(enter_search_app_wait_time)
        except Exception:
            pass



    """
        输入KW内容
    """
    def enter_test_content(self):
        KeyCode.touch_center(self.driver, wait_time=enter_search_app_wait_time, after_time=enter_search_app_wait_time)
        KeyCode.touch_left(self.driver)
        KeyCode.touch_down(self.driver)
        KeyCode.touch_right(self.driver)
        KeyCode.touch_center(self.driver, wait_time=enter_search_app_wait_time, after_time=enter_search_app_wait_time)
        KeyCode.touch_up(self.driver)

    """
        判断是否搜索成功
    """
    def check_search_is_successful(self):
        self.check_has_element_by_text(check_search_is_successful_keyword)

    """
        判断搜索的应用能否正常使用
    """
    def check_search_result_can_use(self):
        self.location_search_app()
        self.check_has_open_search_app_page_and_open_app()
        self.reset_has_opened_search_result_app()

    """
        判断是否能够打开搜索结果的app的应用详情界面，以及打开app
    """
    def check_has_open_search_app_page_and_open_app(self):
        self.check_has_element_by_text(check_search_app_can_show)
        time.sleep(enter_search_app_wait_time)
        KeyCode.touch_center(self.driver, wait_time=enter_search_app_wait_time, after_time=enter_search_app_wait_time)
        start_time = int(time.time())
        while True:
            current_time = int(time.time())
            dif_time = current_time - start_time
            if self.check_search_result_app_has_download_finish():
                break
            if dif_time/60 > down_load_time_out:  # 下载超时
                if self.check_search_result_app_has_download_finish():  # 下载失败
                    raise Exception(load_apk_fail)

        print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。开始拍照")
        ImageUtil.check_video_has_playing_normal(self.driver, need_enter_center=True,
                                                 key_center_wait_time=enter_search_app_wait_time,
                                                 key_center_repeat_count=search_result_app_open_repeat_count)

        time.sleep(enter_search_app_wait_time)
        current_activity_name = self.driver.current_activity
        if current_activity_name != check_open_app_splash_activity_name:  # 根据打开的应用的界面名称匹配是否正确打开应用
            raise Exception(open_apk_fail+"_"+check_search_is_successful_keyword)

        print("获取到的当前界面名称、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、： "+str(current_activity_name))

    """
        退出打开的应用
    """
    def reset_has_opened_search_result_app(self):
        print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。截图完成，开始点击center")
        KeyCode.touch_center(self.driver, wait_time=enter_search_app_wait_time, after_time=enter_search_app_wait_time)
        print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。截图完成，开始点击返回")
        KeyCode.touch_back(self.driver)
        print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。截图完成，开始点击向下")
        KeyCode.touch_down(self.driver, wait_time=enter_search_app_wait_time)
        print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。截图完成，开始点击退出")
        KeyCode.touch_center(self.driver, wait_time=enter_search_app_wait_time, after_time=enter_search_app_wait_time)

    """
        判断应用是否下载成功
    """
    def check_search_result_app_has_download_finish(self):
        try:
            self.check_has_element_by_text(check_search_app_has_download_finish)
            print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。获取到打开")
            return True
        except Exception:
            return False


    """
        定位到搜索的应用
    """
    def location_search_app(self):
        KeyCode.touch_right(self.driver)
        KeyCode.touch_center(self.driver, wait_time=enter_search_app_wait_time, after_time=enter_search_app_wait_time)


    """
        搜索应用位置复位
    """
    def location_reset(self):
        KeyCode.touch_back(self.driver, repeat_count=app_market_location_reset_back_count, wait_time=enter_search_app_wait_time)


