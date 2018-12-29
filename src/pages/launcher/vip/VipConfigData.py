# coding:utf-8
from moudle import HomeTabUtils

__author__ = 'Alan'
'''
description: Launcher VIP配置数据
'''

# VIP海报的定位数据
vip_poster_location = {"key_down_repeat_count": 1, "key_down_wait_time": 1,
                       "key_left_repeat_count": 0, "key_left_wait_time": 0,
                       "key_right_repeat_count": 2, "key_right_wait_time": 0,
                       "key_center_repeat_count": 1, "key_center_wait_time": 0,
                       "key_back_repeat_count": 2, "key_back_wait_time": 0, "wait_time": 2,
                       "tab_index": HomeTabUtils.tab_four, "need_first_back": True}


vip_qr_code_save_path ="D:/Android_AutoTest/test/LaucherTest/src/test_stability/testDemo/screenshot" # 配置截取vip二维码存放的路径


vip_ai_qi_yi_name = "ai_qi_yi"  # 爱奇艺的名称
vip_mang_guo_name = "mang_guo"   # 芒果的名称
vip_sou_hu_name = "sou_hu"       # 搜狐的名称

vip_ai_qi_yi_qr_code_address = "http://tinyurl.ptqy.gitv.tv/c99ZXkg-93a613b5"  # 爱奇艺 的二维码地址
vip_mang_guo_qr_code_address = "http://weixin.qq.com/q/02slDydTeXbjT13NSDNs1u"  # 芒果 的二维码地址
vip_sou_Hu_qr_code_address = "https://h5.ott.tv.sohu.com/snm/user/views/login.html?qrcode=0873f7a587a69bc576855ef450e09564&back_uri=https%3A%2F%2Fh5.ott.tv.sohu.com%2Fsnm%2Fuser%2Fviews%2Fpay.html%3Fqrcode%3D0873f7a587a69bc576855ef450e09564%26pay_type%3Drenew%26v%3D6.5.0.1"  # 搜狐 的二维码地址

vip_qr_code_scan_fail = "vip会员二维码扫描失败"

vip_ai_qi_yi_pic_name = "ai_qi_yi"  # 截取爱奇艺的二维码图片的名称
vip_mang_guo_pic_name = "mang_guo"   # 截取芒果的二维码图片的名称
vip_sou_hu_pic_name = "sou_hu"       # 截取搜狐的二维码图片的名称

wait_time = "3"  # 函数执行前的时间
touch_right_wait_time = 3  # 点击右键前等待的时间
vip_enter_after_time = 8    # 进入vip界面后sleep的时间
vip_enter_repeat_count = 2


vip_ai_qi_yi_app_open_activity_name = "com.gala.video.app.epg.web.WebCommonActivity"  # 爱奇艺会员界面
vip_mang_guo_app_open_activity_name = ".ui.activity.VipLoginActivity"  # 芒果会员界面
vip_sou_hu_app_open_activity_name = ".activity.PayActivity"  # 搜狐会员界面


vip_open_fail = "vip会员界面打开失败"

reset_back_repeat_count = 4  # 点击完海报后按下返回键的次数

