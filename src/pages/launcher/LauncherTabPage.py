# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher Tab切换测试
'''

from general.Base_page import Base
from moudle.HomeTabUtils import TabUtils
from general.KeyCodeSentUtils import *
from general import Utils as U


class LauncherTab(Base):

    search_text = '如需搜索：“极米”'  # 搜索 固定的关键字
    more_text = '视频应用'  # 更多 固定的关键字
    my_text = '我的精选'  # 我的 固定的关键字
    vip_text = 'VIP热播榜'  # VIP 固定的关键字
    movie_text = '最新热门影片'  # movie 固定的关键字
    child_text = '小朋友都爱看'  # 少儿 固定的关键字
    tv_series_text = '海外剧场'  # 电视剧 固定的关键字
    variety_text = '强档综艺'  # 综艺 固定的关键字
    sport_text = '最热赛事'  # 体育 固定的关键字
    four_k_text = '4k免费试看专区'  # 4k 固定的关键字
    app_text = '本地应用'  # 应用 固定的关键字

    tab_text_list = [search_text, more_text, my_text, vip_text, movie_text, child_text, tv_series_text, variety_text,
                     sport_text, four_k_text, app_text]  # 按照Launcher 的Tab从左到右的顺序写 切记一定按照顺序

    tab_down_count_list = [0, 6, 0, 3, 4, 4, 7, 5, 0, 0, 0]  # 每个Tab需要通过遥控器的下键移动多少步骤才能展现要找的文本View, 该数组大小需要与tab_text_list数组大小一样，并且下标一一对应

    key_down_wait_time = 1
    key_back_wait_time = 2
    key_right_wait_time = 1
    function_perform_time = 2

    """
    从Tab栏的左边往右点击，
    wait_time = 函数执行前等待的时间
    """
    def click_tab_from_left_to_right(self, wait_time=function_perform_time):
        time.sleep(wait_time)
        for text in self.tab_text_list:
            touch_down_count = self.tab_text_list.index(text)

            if touch_down_count == 0:  # 跳转到第一个Tab
                TabUtils.click_tab_one(self.driver)

            if touch_down_count != 0:
                KeyCode.touch_down(self.driver, wait_time=self.key_down_wait_time, repeat_count=self.tab_down_count_list[touch_down_count])  # 根据Tab中的切换成功标志的位移个数进行向下位移

            U.Logging.error("获取的元素位置:  " + str(touch_down_count))
            self.check_has_element_by_text(text)
            KeyCode.touch_back(self.driver, wait_time=self.key_back_wait_time)
            KeyCode.touch_right(self.driver, wait_time=self.key_right_wait_time)





