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



# 应用更新测试用例数据
update_all_view_resource_id = "com.xgimi.home:id/lb_updateapklist_updateall"  # 应用全部更新的View ID
update_all_number_view_resource_id = "com.xgimi.home:id/lb_updateapklist_num"  # 展示可更新应用数量的ID
update_all_app_view_keyword = "全部更新"  # 应用全部更新的关键字
update_one_app_view_keyword = "更新"  # 单个应用更新的关键字
update_all_app_fail = "更新全部应用失败"  # 更新应用失败后抛出异常的关键字
update_one_app_fail = "更新单个应用失败"  # 更新应用失败后抛出异常的关键字
check_update_all_app_wait_time = 5  # 检测更新全部应用，退出进入应用管理的间隔时间
check_update_all_app_count = 5  # 检测更新全部应用，退出进入应用管理的最大次数，超过这个次数
no_need_update_apps = "没有需要更新的应用"

app_manage_location_reset_back_count = 4  # 应用市场位置复位返回键的重复次数



# 应用卸载测试用例数据
unintall_app_view_recource_id = "com.android.packageinstaller:id/ok_button"  # 应用卸载弹框的下一步view的ID
uninstall_app_view_app_name_resource_id = "com.android.packageinstaller:id/app_name"  # 应用卸载弹框的显示应用名称view的ID
uninstall_later_wait_time = 3  # 卸载完后等待时间
uninstall_app_button_view_id = "com.xgimi.home:id/item_localapk_btn_uninstall"  # 卸载按钮view的ID

uninstall_app_button_attribute = "focusable"  # 判断系统应用是否能够卸载的属性
uninstall_app_button_attribute_value = "true"  # 判断系统应用是否能够卸载的属性的值
system_app_can_uninstall = "系统应用卸载按钮可以获取焦点"

uninstall_system_app_name = "电子说明书"  # 需要测试的应用卸载的系统app名称





# 应用停止测试用例数据
stop_app_name = "QQ音乐"  # 需要停止的应用的名称
stop_app_process_name = "hk.reco.qqmusic"  # 需要停止的应用进程的名称
stop_app_view_id = "com.xgimi.home:id/item_localapk_btn_stop"  # 停止进程按钮的view的ID
stop_app_name_text_view_id = "com.xgimi.home:id/item_localapk_name" # 需要停止的应用的显示应用名称的view的ID
stop_app_view_text = "强行停止"   # 停止进程按钮的text
get_view_attribute_bounds = "bounds"  # 获取view的bounds属性
stop_app_fail_message = "停止应用进程失败"


clear_data_view_id = "com.xgimi.home:id/item_localapk_btn_cleardata"  # 清除应用数据的view的ID
clear_data_view_text = "清除数据"   # 清除应用数据的view的text


# 应用数据清除测试用例数据
permission_dialog_allow_button_resource_id =  "com.android.packageinstaller:id/permission_allow_button"
clear_data_test_app_name = "WPS 投影宝"
enter_app_later_wait_time = 3  # 打开需要清除的应用后等待的时间
clear_app_data_fail = "清除应用数据失败"



