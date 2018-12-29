# coding:utf-8
from general.ImageUtils import ImageUtil

__author__ = 'Alan'
'''
description: Launcher VIP 奇异果、芒果、搜索会员确定
'''
from moudle import HomeTabUtils, LauncherUtils
from moudle.LauncherBasePage import LauncherBasePage
from general import QrScanUtils, Utils
from moudle.LauncherBasePage import LauncherBasePage
from src.pages.launcher.vip.VipConfigData import *

from general.KeyCodeSentUtils import *
def test():
    path = QrScanUtils.qr_code_scan("Android_AutoTest/test/LaucherTest/screenshot/ai_qi_yi.png")
    print(path)




class VipConfirm(LauncherBasePage):

    """
        定位到vip跳转海报
    """
    def location_vip_poster(self):
        LauncherUtils.move_to_target_location(driver=self.driver,
                                              key_down_repeat_count=vip_poster_location["key_down_repeat_count"],
                                              key_down_wait_time=vip_poster_location["key_down_wait_time"],
                                              key_left_repeat_count=vip_poster_location["key_left_repeat_count"],
                                              key_left_wait_time=vip_poster_location["key_left_wait_time"],
                                              key_right_repeat_count=vip_poster_location["key_right_repeat_count"],
                                              key_right_wait_time=vip_poster_location["key_right_wait_time"],
                                              key_center_repeat_count=vip_poster_location["key_center_repeat_count"],
                                              key_center_wait_time=vip_poster_location["key_center_wait_time"],
                                              key_back_repeat_count=vip_poster_location["key_back_repeat_count"],
                                              key_back_wait_time=vip_poster_location["key_back_wait_time"],
                                              wait_time=vip_poster_location["wait_time"],
                                              tab_index=vip_poster_location["tab_index"],
                                              need_first_back=vip_poster_location["need_first_back"])

    def test_confirm_vip_open_normal_and_qrcode_can_scan(self):

        self.check_ai_qi_yi_open_and_rc_code()

        self.check_mang_guo_open_and_rc_code()

        self.check_sou_hu_open_and_rc_code()

        self.location_reset()

    """
        检测 搜狐 的打开与二维码扫码
    """
    def check_sou_hu_open_and_rc_code(self):
        KeyCode.touch_right(self.driver, wait_time=touch_right_wait_time)
        KeyCode.touch_center(self.driver)
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。目前的界面:  " + str(self.driver.current_activity) + "    high:  ")
        self.check_vip_open_normal(vip_sou_hu_name)
        sou_hu_path = ImageUtil.screen_shot_by_location(self.driver, src_path=vip_qr_code_save_path,
                                                        src_name=vip_sou_hu_pic_name)
        self.check_vip_qr_code_scan_normal(vip_sou_hu_name, sou_hu_path)
        KeyCode.touch_back(self.driver, wait_time=vip_enter_after_time)

    """
        检测 芒果 的打开与二维码扫码
    """
    def check_mang_guo_open_and_rc_code(self):
        KeyCode.touch_right(self.driver, wait_time=touch_right_wait_time)
        KeyCode.touch_center(self.driver)
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。目前的界面:  " + str(self.driver.current_activity) + "    high:  ")
        self.check_vip_open_normal(vip_mang_guo_name)
        mang_guo_path = ImageUtil.screen_shot_by_location(self.driver, src_path=vip_qr_code_save_path,
                                                          src_name=vip_mang_guo_pic_name)
        self.check_vip_qr_code_scan_normal(vip_mang_guo_name, mang_guo_path)
        KeyCode.touch_back(self.driver, wait_time=vip_enter_after_time)

    """
        检测 爱奇艺 的打开与二维码扫码
    """
    def check_ai_qi_yi_open_and_rc_code(self):
        KeyCode.touch_center(self.driver, wait_time=wait_time)
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。目前的界面:  " + str(self.driver.current_activity) + "    high:  ")
        self.check_vip_open_normal(vip_ai_qi_yi_name)
        ai_qi_yi_path = ImageUtil.screen_shot_by_location(self.driver, src_path=vip_qr_code_save_path,
                                                          src_name=vip_ai_qi_yi_pic_name)
        self.check_vip_qr_code_scan_normal(vip_ai_qi_yi_name, ai_qi_yi_path)
        KeyCode.touch_back(self.driver, wait_time=vip_enter_after_time)

    """
        判断vip  二维码 是否成功扫描
        vip_name: 需要判断的vip名称
        src_path： 截取的二维码图片地址
    """
    def check_vip_qr_code_scan_normal(self, vip_name, src_path):
        time.sleep(wait_time)
        qr_code_address = QrScanUtils.qr_code_scan(src_path)
        if vip_name == vip_ai_qi_yi_name:  # 爱奇艺 二维码 判断
            if vip_ai_qi_yi_qr_code_address != vip_ai_qi_yi_app_open_activity_name:
                raise Exception(vip_qr_code_scan_fail+"_"+vip_ai_qi_yi_name)
        elif vip_name == vip_mang_guo_name:  # 芒果 二维码 判断
            if qr_code_address != vip_mang_guo_qr_code_address:
                raise Exception(vip_qr_code_scan_fail+"_"+vip_mang_guo_name)
        elif vip_name == vip_sou_hu_name:   # 搜狐 二维码 判断
            if qr_code_address != vip_sou_Hu_qr_code_address:
                raise Exception(vip_qr_code_scan_fail+"_"+vip_sou_hu_name)
        time.sleep(wait_time)

    """
        判断vip界面是否成功打开
        vip_name: 需要判断的vip名称
    """
    def check_vip_open_normal(self, vip_name):
        time.sleep(wait_time)
        current_activity_name = self.driver.current_activity
        if vip_name == vip_ai_qi_yi_name:  # 爱奇艺界面判断
            if current_activity_name != vip_ai_qi_yi_app_open_activity_name:
                raise Exception(vip_open_fail+"_"+vip_ai_qi_yi_name)
        elif vip_name == vip_mang_guo_name:  # 芒果界面判断
            if current_activity_name != vip_mang_guo_app_open_activity_name:
                raise Exception(vip_open_fail+"_"+vip_mang_guo_name)
        elif vip_name == vip_sou_hu_name:   # 搜狐界面判断
            if current_activity_name != vip_sou_hu_app_open_activity_name:
                raise Exception(vip_open_fail+"_"+vip_sou_hu_name)
        time.sleep(wait_time)
    """
        位置复位
    """
    def location_reset(self):
        KeyCode.touch_back(self.driver, repeat_count=reset_back_repeat_count, wait_time=wait_time)
