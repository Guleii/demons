# coding:utf-8
import time

__author__ = 'Alan'
'''
description: Launcher 的basePage
'''
from general.Base_page import Base
from moudle import LauncherUtils
from general.KeyCodeSentUtils import KeyCode
from moudle import HomeTabUtils
from moudle import HomeTabUtils


class LauncherBasePage(Base):

    # 分别对应Launcher的Tab_index
    tab_one = HomeTabUtils.tab_one
    tab_two = HomeTabUtils.tab_two
    tab_three = HomeTabUtils.tab_three
    tab_four = HomeTabUtils.tab_four
    tab_five = HomeTabUtils.tab_five
    tab_six = HomeTabUtils.tab_six
    tab_seven = HomeTabUtils.tab_seven
    tab_eight = HomeTabUtils.tab_eight
    tab_nine = HomeTabUtils.tab_nine
    tab_ten = HomeTabUtils.tab_ten
    tab_eleven = HomeTabUtils.tab_eleven

    target_text = '腾讯专区'  # 跳转是否成功的比对值
    function_perform_time = 2  # 函数执行前需要等待的时间
    key_down_count = 1  # 需要按下遥控器的下键几次才能到达目标海报
    tab_index = HomeTabUtils.tab_two  # 目标海报位于那个Tab下
    key_back_wait_time = 2
    key_back_repeat_count = 0
    key_down_wait_time = 1
    key_down_repeat_count = 0
    key_left_wait_time = 2
    key_left_repeat_count = 0
    key_right_wait_time = 2
    key_right_repeat_count = 0
    key_center_wait_time = 3
    key_center_repeat_count = 0

    you_ku = "com.cibn.tv"

    yun_shi_ting_ji_guang = "com.ktcp.tvvideo"  # 云视听极光
    cibn_ku_miao_ying_shi = "com.cibn.tv"  # CIBN酷喵影视
    yun_shi_ting_dian_shi_mao = "com.moretv.android"  # 云视听电视猫
    yun_shi_ting_yue_ting_tv = "com.sohuott.tv.vod"  # 云视听悦厅TV
    fit_time = "com.fittime.tv.common"  # FitTime
    pptv_ju_ti_yu = "com.pptv.tvsports"  # PPTV聚体育（CIBN聚体育）
    cibn_4k_hua_yuan = "net.cibntv.ott.sk"  # CIBN4K花园
    yu_jia_tv = "com.yogafittime.tv.common"  # 瑜伽TV
    liu_xing_wu_tv = "com.dance.fittime.tv.common"  # 流行舞TV
    you_le_dou_di_zhu = "com.youjoy.strugglelandlord"  # 有乐斗地主
    bai_shi_tong_tv = "com.bestv.ott.baseservices"  # 百视通TV
    bi_li_bi_li_tv = "com.xiaodianshi.tv.yst"  # 哔哩哔哩TV版
    xiao_yao_jie_wu = "com.streetdance.fittime.tv.common"  # 小腰街舞

    def move_to_target(self, key_down_repeat_count=key_down_repeat_count,
                       key_down_wait_time=key_down_wait_time,
                       key_left_repeat_count=key_left_repeat_count,
                       key_left_wait_time=key_left_wait_time,
                       key_right_repeat_count=key_right_repeat_count,
                       key_right_wait_time=key_right_wait_time,
                       tab_index=tab_index,
                       key_back_repeat_count=key_back_repeat_count,
                       wait_time=function_perform_time):
        LauncherUtils.move_to_target_location(driver=self.driver,
                                              key_down_repeat_count=key_down_repeat_count,
                                              key_down_wait_time=key_down_wait_time,
                                              key_left_repeat_count=key_left_repeat_count,
                                              key_left_wait_time=key_left_wait_time,
                                              key_right_repeat_count=key_right_repeat_count,
                                              key_right_wait_time=key_right_wait_time,
                                              key_back_repeat_count=key_back_repeat_count,
                                              tab_index=tab_index,
                                              wait_time=wait_time)

    def touch_back(self, key_back_repeat_count=key_back_repeat_count, key_back_wait_time=key_back_wait_time):
        KeyCode.touch_back(self.driver, key_back_repeat_count, key_back_wait_time)

    """
        根据影视应用的包名返回
    """
    def touch_back_by_package_name(self, package_name, wait_time=key_back_wait_time):
        time.sleep(wait_time)
        if package_name == self.cibn_ku_miao_ying_shi or package_name == self.yun_shi_ting_yue_ting_tv or package_name == self.bi_li_bi_li_tv:  # CIBN酷喵影视、云视听悦听、哔哩哔哩 先按返回-再按OK键-再按返回
            self.touch_back(key_back_repeat_count=1, key_back_wait_time=1)
            KeyCode.touch_center(self.driver, wait_time=2)
            self.touch_back(key_back_repeat_count=1, key_back_wait_time=1)

        elif package_name == self.yun_shi_ting_dian_shi_mao:  # 云视听电视猫 按两次次返回键
            self.touch_back(key_back_repeat_count=2, key_back_wait_time=0)
            self.touch_back(key_back_repeat_count=1, key_back_wait_time=1)

        elif package_name == self.bai_shi_tong_tv or package_name == self.yun_shi_ting_ji_guang:  # 百事通TV、云视听极光   按一次返回键
            self.touch_back(key_back_repeat_count=1, key_back_wait_time=0)
            self.touch_back(key_back_repeat_count=1, key_back_wait_time=2)

        elif package_name == self.fit_time:  # Fit time  先按返回-再按右键-再按OK键-再按返回
            self.touch_back(key_back_repeat_count=1, key_back_wait_time=1)
            KeyCode.touch_right(self.driver, wait_time=1)
            KeyCode.touch_center(self.driver, wait_time=2)
            self.touch_back(key_back_repeat_count=1, key_back_wait_time=1)
        elif package_name == self.pptv_ju_ti_yu:  # CIBN聚体育  先按两次返回-再按右键-再按OK键-再按返回
            self.touch_back(key_back_repeat_count=2, key_back_wait_time=1)
            KeyCode.touch_center(self.driver, wait_time=2)
            self.touch_back(key_back_repeat_count=1, key_back_wait_time=1)
