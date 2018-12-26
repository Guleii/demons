# coding:utf-8

__author__ = 'Alan'
'''
description: Launcher 单张海报点击应用跳转测试
'''
from moudle.LauncherBasePage import LauncherBasePage
from general.Base_page import Base
from moudle.HomeTabUtils import TabUtils
from moudle import HomeTabUtils
from moudle import LauncherUtils

from general.KeyCodeSentUtils import *
from general import Utils as U
from general.AdbUtils import ADB
from general.ImageUtils import ImageUtil
import config.GlobalConfig as gl


"""
progressBar=MaterialProgressBar
ivIcon=CircleImageView
ivIconProgressBg=CircleProgressBar
ivIconProgress=CircleProgressBar
tvName、tvProgress=TextView

"""


class SingleAppPosterJump(LauncherBasePage):
        window_location = [(1562, 1010), (1818, 1000)]
        you_ku = "com.cibn.tv"

        yun_shi_ting_ji_guang = "com.ktcp.tvvideo"   # 云视听极光
        cibn_ku_miao_ying_shi = "com.cibn.tv"  # CIBN酷喵影视
        yun_shi_ting_dian_shi_mao = "com.moretv.android"  # 云视听电视猫
        yun_shi_ting_yue_ting_tv = "com.sohuott.tv.vod"  # 云视听悦厅TV
        fit_time = "com.fittime.tv.common"  # FitTime
        pptv_ju_ti_yu = "com.pptv.tvsports"  # PPTV聚体育
        cibn_4k_hua_yuan = "net.cibntv.ott.sk"  # CIBN4K花园
        yu_jia_tv = "com.yogafittime.tv.common"  # 瑜伽TV
        liu_xing_wu_tv = "com.dance.fittime.tv.common"  # 流行舞TV
        you_le_dou_di_zhu = "com.youjoy.strugglelandlord"  # 有乐斗地主
        bai_shi_tong_tv = "com.bestv.ott.baseservices"  # 百视通TV
        bi_li_bi_li_tv = "com.xiaodianshi.tv.yst"  #  哔哩哔哩TV版
        xiao_yao_jie_wu = "com.streetdance.fittime.tv.common"  # 小腰街舞

        down_load_time_out = 1  # 下载超时时间单位/分钟

        load_apk_fail = "应用下载失败应用包名： "
        open_apk_fail = "没有正确打开第三方应用： "

        def test_load_or_enter_video_app(self, app_package=you_ku, wait_time=LauncherBasePage.function_perform_time,
                                         tab_index=HomeTabUtils.tab_one,
                                         key_down_wait_time=LauncherBasePage.key_down_wait_time,
                                         key_down_repeat_count=LauncherBasePage.key_down_repeat_count,
                                         key_left_wait_time=LauncherBasePage.key_left_wait_time,
                                         key_left_repeat_count=LauncherBasePage.key_left_repeat_count,
                                         key_back_repeat_count=LauncherBasePage.key_back_repeat_count,
                                         key_right_wait_time=LauncherBasePage.key_right_wait_time,
                                         key_right_repeat_count=LauncherBasePage.key_right_repeat_count,
                                         need_first_back=True):
                if need_first_back:
                        self.touch_back(key_back_repeat_count=2)
                self.move_to_target(key_down_repeat_count=key_down_repeat_count,
                                    key_down_wait_time=key_down_wait_time,
                                    key_left_repeat_count=key_left_repeat_count,
                                    key_left_wait_time=key_left_wait_time,
                                    key_right_repeat_count=key_right_repeat_count,
                                    key_right_wait_time=key_right_wait_time,
                                    key_back_repeat_count=key_back_repeat_count,
                                    tab_index=tab_index,
                                    wait_time=wait_time,
                                    need_first_back=need_first_back)
                self.check_enter_or_load(app_package)

                # self.touch_back(key_back_repeat_count=2)

        def check_enter_or_load(self, app_package):
                adb = ADB(gl.test_app_more_device_device_name)
                app = adb.get_third_app_list()
                fail_tip = self.load_apk_fail + app_package
                # current_activity = self.driver.current_activity
                U.Logging.error("应用：" + app)
                if app_package in app:
                        self.enter_video_app(adb, app_package=app_package)
                        if self.fit_time == app_package or self.bi_li_bi_li_tv == app_package:
                                self.touch_back(key_back_repeat_count=3)
                        else:
                                self.touch_back_by_package_name(app_package)
                else:
                        KeyCode.touch_center(self.driver, wait_time=1, after_time=1)

                        #不要删除一下代码 ，一下代码是另一种判断下载框是否弹出的条件
                        # KeyCode.touch_center(self.driver, wait_time=1, after_time=2)
                        # self.check_has_element_by_text("CIBN酷喵影视")
                        # enter_activity = self.driver.current_activity
                        # if current_activity != enter_activity:
                        #         raise Exception(self.load_apk_fail + app_package)

                        if ImageUtil.check_video_has_playing_normal(driver=self.driver,perform_first_screen_shot_wait_time=1, perform_second_screen_shot_wait_time=3):
                                pass
                        else:
                                start_time = int(time.time())
                                while True:
                                        current_time = int(time.time())
                                        dif_time = current_time - start_time
                                        app_list_now = adb.get_third_app_list()
                                        if app_package in app_list_now:
                                                self.enter_video_app(adb, app_package=app_package)
                                                self.touch_back_by_package_name(app_package)
                                                break
                                        elif dif_time / 60 > self.down_load_time_out:  # 下载超时
                                                if ImageUtil.check_video_has_playing_normal(driver=self.driver,
                                                                                            perform_first_screen_shot_wait_time=1,
                                                                                            perform_second_screen_shot_wait_time=10,
                                                                                            err_message=fail_tip):
                                                        pass
                                                else:
                                                        raise Exception(fail_tip)



        def enter_video_app(self, adb, app_package=you_ku):
                U.Logging.error("已经包含优酷：11")
                KeyCode.touch_center(self.driver, wait_time=1, after_time=3)
                current_activity_package_name = adb.get_current_package_name()
                if app_package not in current_activity_package_name:
                        raise Exception(self.open_apk_fail+app_package)



        # def test_load_or_enter_sport_app(self):
        #         self.move_to_target(tab_index=LauncherBasePage.tab_eleven, key_down_repeat_count=1,
        #                             key_left_repeat_count=0, key_right_repeat_count=2)
        #         KeyCode.touch_center(self.driver)
        #         self.check_enter_or_load(self.fit_time)
