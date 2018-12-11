# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher测试
'''

from general.Base_page import Base
from moudle.HomeTabUtils import TabUtils
from general.KeyCodeSentUtils import *


class LauncherTab(Base):

    search_text = '如需搜索：“极米”'  # 搜索 固定的关键字
    more_text = '视频应用'  # 更多 固定的关键字
    my_text = '我的精选'  # 我的 固定的关键字
    vip_text = 'VIP热播榜'  # VIP 固定的关键字
    movie_text = '最新热门电影'  # movie 固定的关键字
    child_text = '小朋友都爱看'  # 少儿 固定的关键字
    tv_series = '海外剧场'  # 电视剧 固定的关键字
    variety_text = '强档综艺'  # 综艺 固定的关键字
    sport_text = '最热赛事'  # 体育 固定的关键字
    four_k_text = '4k免费试看专区'  # 4k 固定的关键字
    app_text = '本地应用'  # 应用 固定的关键字

    def click_from_left_to_right(self):
        # TabUtils.click_tab_one(self.driver)
        # self.check_has_element_by_text(self.search_text,wait_time=2)

        TabUtils.click_tab_two(self.driver)
        KeyCode.touch_down(self.driver, wait_time=1, repeat_count=6)
        self.check_has_element_by_text(self.more_text)
        time.sleep(5)




