# coding:utf-8
__author__ = 'Alan'
'''
description: 应用管理 --》数据配置
'''
from moudle import HomeTabUtils

# 应用市场搜索的定位数据
app_market_location = {"key_down_repeat_count": 1, "key_down_wait_time": 1,
                       "key_left_repeat_count": 1, "key_left_wait_time": 0,
                       "key_right_repeat_count": 0, "key_right_wait_time": 0,
                       "key_center_repeat_count": 1, "key_center_wait_time": 0,
                       "key_back_repeat_count": 2, "key_back_wait_time": 0, "wait_time": 2,
                       "tab_index": HomeTabUtils.tab_eleven, "need_first_back": True}

enter_manage_app_wait_time = 2  # 进入应用管理的等待时间
after_enter_manage_app_wait_time = 2  # 进入应用管理后的等待时间

update_all_view_resource_id = "com.xgimi.home:id/lb_updateapklist_updateall"  # 应用全部更新的View ID
update_all_number_view_resource_id = "com.xgimi.home:id/lb_updateapklist_num"  # 展示可更新应用数量的ID
update_all_app_view_keyword = "全部更新"  # 应用全部更新的关键字
update_one_app_view_keyword = "更新"  # 单个应用更新的关键字
update_all_app_fail = "更新全部应用失败"  # 更新应用失败后抛出异常的关键字
update_one_app_fail = "更新单个应用失败"  # 更新应用失败后抛出异常的关键字

check_update_all_app_wait_time = 5  # 检测更新全部应用，退出进入应用管理的间隔时间
check_update_all_app_count = 5  # 检测更新全部应用，退出进入应用管理的最大次数，超过这个次数


no_need_update_apps = "没有需要更新的应用"

app_manage_location_reset_back_count = 2  # 应用市场位置复位返回键的重复次数




unintall_app_view_recource_id = "com.android.packageinstaller:id/ok_button"  # 应用卸载弹框的下一步view的ID

uninstall_app_view_app_name_resource_id = "com.android.packageinstaller:id/app_name"  # 应用卸载弹框的显示应用名称view的ID

uninstall_later_wait_time = 3  # 卸载完后等待时间



stop_app_name = "QQ音乐"  # 需要停止的应用的名称
stop_app_process_name = "hk.reco.qqmusic"  # 需要停止的应用进程的名称
