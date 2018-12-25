# coding:utf-8
__author__ = 'Alan'
'''
description: 应用市场 --》数据配置
'''
from moudle import HomeTabUtils

# 应用市场搜索的定位数据
app_market_location = {"key_down_repeat_count": 1, "key_down_wait_time": 1,
                       "key_left_repeat_count": 0, "key_left_wait_time": 0,
                       "key_right_repeat_count": 0, "key_right_wait_time": 0,
                       "key_center_repeat_count": 1, "key_center_wait_time": 0,
                       "key_back_repeat_count": 2, "key_back_wait_time": 0, "wait_time": 2,
                       "tab_index": HomeTabUtils.tab_eleven, "need_first_back": True}

enter_search_app_wait_time = 2  # 进入搜索的等待时间

check_search_is_successful_keyword = "酷我K歌TV版"  # 判断是否搜索成功的关键字
check_search_app_can_show = "下载"  # 判断是搜索的应用界面能否展示的关键字
check_search_app_has_download_finish = "打开"  # 判断是搜索的应用界面能否展示的关键字
search_result_app_open_repeat_count = 2  # 打开搜索应用的按下center键的次数
load_apk_fail = "应用下载失败 "  # 应用下载失败

down_load_time_out = 3  # 下载超时时间单位/分钟

app_market_location_reset_back_count = 4  # 应用市场位置复位返回键的重复次数
