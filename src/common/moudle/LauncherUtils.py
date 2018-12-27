# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher 多级海报点击跳转测试
'''

from general.Base_page import Base
from moudle.HomeTabUtils import TabUtils
from moudle import HomeTabUtils
from general import Utils

from general.KeyCodeSentUtils import *
from general.Utils import check_has_element_by_text

open_app_name ="WPS 投影宝"
can_find_app = "找不到"
find_app_count = 30  # 寻找指定app向下位移的最大次数，超过此次数，若还找不到应用则抛出异常
def move_to_target_location(driver, key_down_repeat_count=0, key_down_wait_time=1, key_left_repeat_count=0,
                            key_left_wait_time=1, key_right_repeat_count=0, key_right_wait_time=1, tab_index=1,
                            wait_time=2,
                            key_center_repeat_count=0, key_center_wait_time=0,
                            key_back_repeat_count=2,
                            key_back_wait_time=0,
                            need_first_back=True):
    time.sleep(wait_time)
    if need_first_back:
        KeyCode.touch_back(driver, wait_time=key_down_wait_time, repeat_count=key_back_repeat_count)
    if tab_index == HomeTabUtils.tab_two:
        TabUtils.click_tab_by_input_index(driver, HomeTabUtils.tab_eleven)
    else:
        TabUtils.click_tab_by_input_index(driver, HomeTabUtils.tab_one)
    time.sleep(wait_time)
    TabUtils.click_tab_by_input_index(driver, tab_index)

    KeyCode.touch_down(driver, wait_time=key_down_wait_time, repeat_count=key_down_repeat_count)
    KeyCode.touch_left(driver, wait_time=key_left_wait_time, repeat_count=key_left_repeat_count)
    KeyCode.touch_right(driver, wait_time=key_right_wait_time, repeat_count=key_right_repeat_count)
    KeyCode.touch_center(driver, wait_time=key_center_wait_time, repeat_count=key_center_repeat_count)


"""
    打开Launcher 应用Tag栏下面的应用
    app_name: 需要打开的应用名称
    wait_time： 函数执行前等待的时间
    key_center_wait_time： 点击OK键之前等待的时间
    need_first_back： 执行函数前是否需要复位
    tab_index： 需要跳转的tab栏的下标
    key_back_wait_time： 点击返回键前等待的时间
    key_back_repeat_count： 点击返回键的次数
    
"""


def open_launcher_app_tab_app(driver, app_name=open_app_name, wait_time=2, key_down_wait_time=1, key_center_wait_time=0,
                              need_first_back=True, tab_index=1, key_back_wait_time=0, key_back_repeat_count=2):
    time.sleep(wait_time)
    if need_first_back:
        KeyCode.touch_back(driver, wait_time=key_back_wait_time, repeat_count=key_back_repeat_count)
    if tab_index == HomeTabUtils.tab_two:
        TabUtils.click_tab_by_input_index(driver, HomeTabUtils.tab_eleven)
    else:
        TabUtils.click_tab_by_input_index(driver, HomeTabUtils.tab_one)
    time.sleep(wait_time)
    TabUtils.click_tab_by_input_index(driver, tab_index)
    find_count = 0
    while True:
        KeyCode.touch_down(driver, wait_time=key_down_wait_time)
        find_count += 1
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。查找指定的元素： "+app_name)
        try:
            check_has_element_by_text(driver=driver, text=app_name).click()
            Utils.Logging.info("。。。。。。。。。。。。。。。。。。。找到元素： " + app_name)
            time.sleep(wait_time)
            KeyCode.touch_center(driver, wait_time=key_center_wait_time, after_time=wait_time)
            Utils.Logging.info("。。。。。。。。。。。。。。。。。。。点击指定的元素： " + app_name)
            # KeyCode.touch_home(driver)
            break
        except Exception:
            pass
        if find_count > find_app_count:
            raise Exception(can_find_app+app_name)







