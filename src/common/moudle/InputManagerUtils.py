# coding:utf-8
from general import Utils

__author__ = 'Alan'
'''
description:主界面输入法的工具类
'''


import time



# 键盘坐标（分辨率1920*1080）
oneLocation = [(101, 355), (209, 441)]
twoLocation = [(253, 355), (361, 441)]
threeLocation = [(405, 355), (513, 441)]
fourLocation = [(101, 485), (209, 571)]
fiveLocation = [(253, 485), (361, 571)]
sixLocation = [(407, 485), (515, 571)]
sevenLocation = [(101, 615), (209, 701)]
eightLocation = [(253, 615), (361, 701)]
nineLocation = [(407, 615), (515, 701)]
tenLocation = [(101, 745), (209, 831)]
elevenLocation = [(253, 745), (361, 831)]
twelveLocation = [(407, 745), (515, 831)]

# # 键盘坐标（分辨率1920*1080）
# oneLocation = [(101, 355), (209, 441)]
# twoLocation = [(253, 355), (361, 441)]
# threeLocation = [(405, 355), (513, 441)]
# fourLocation = [(101, 485), (209, 571)]
# fiveLocation = [(253, 485), (361, 571)]
# sixLocation = [(407, 485), (515, 571)]
# sevenLocation = [(101, 615), (209, 701)]
# eightLocation = [(253, 615), (361, 701)]
# nineLocation = [(407, 615), (515, 701)]
# tenLocation = [(101, 745), (209, 831)]
# elevenLocation = [(253, 745), (361, 831)]
# twelveLocation = [(407, 745), (515, 831)]

# 键盘坐标（分辨率1280*800）
# oneLocation = [(67, 236), (139, 293)]
# twoLocation = [(168, 236), (240, 293)]
# threeLocation = [(269, 236), (341, 293)]
# fourLocation = [(67, 322), (139, 379)]
# fiveLocation = [(168, 322), (240, 379)]
# sixLocation = [(271, 322), (343, 379)]
# sevenLocation = [(67, 409), (139, 466)]
# eightLocation = [(168, 409), (240, 466)]
# nineLocation = [(271, 409), (343, 466)]
# tenLocation = [(67, 496), (139, 553)]
# elevenLocation = [(168, 496), (240, 553)]
# twelveLocation = [(271, 496), (343, 553)]

# 键盘坐标（分辨率1280*720）
# oneLocation = [(67, 236), (139, 293)]
# twoLocation = [(168, 236), (240, 293)]
# threeLocation = [(269, 236), (341, 293)]
# fourLocation = [(67, 322), (139, 379)]
# fiveLocation = [(168, 322), (240, 379)]
# sixLocation = [(271, 322), (343, 379)]
# sevenLocation = [(67, 409), (139, 466)]
# eightLocation = [(168, 409), (240, 466)]
# nineLocation = [(271, 409), (343, 466)]
# tenLocation = [(67, 496), (139, 553)]
# elevenLocation = [(168, 496), (240, 553)]
# twelveLocation = [(271, 496), (343, 553)]

# global oneLocation
# global twoLocation
# global threeLocation
# global fourLocation
# global fiveLocation
# global sixLocation
# global sevenLocation
# global eightLocation
# global nineLocation
# global tenLocation
# global elevenLocation
# global twelveLocation





# 点击某一个输入前默认的等待的时间
defaultWaitTime = 3
# 点击某一个输入后默认的等待的时间
defaultAfterWaitTime = 0


can_get_device_screen_size = "无法获取屏幕分辨率"


"""
    根据屏幕分辨率动态选择坐标

"""


def choose_location_by_device_screen_size(screen_size=[]):
    global oneLocation
    global twoLocation
    global threeLocation
    global fourLocation
    global fiveLocation
    global sixLocation
    global sevenLocation
    global eightLocation
    global nineLocation
    global tenLocation
    global elevenLocation
    global twelveLocation

    Utils.Logging.info("。。。。。。。。。。。。。。。。。。。width:  开始区别分辨率" + "   " + str(screen_size))
    # tenLocation = [(101, 745), (209, 831)]
    width = '1920'
    high = '1080'
    if len(screen_size) == 2:
        width = screen_size[0]
        high = screen_size[1]
    else:
        raise Exception(can_get_device_screen_size)

    if width == '1920' and high == '1080':
        # 键盘坐标（分辨率1920*1080）
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。width:  开始赋值")
        oneLocation = [(101, 355), (209, 441)]
        twoLocation = [(253, 355), (361, 441)]
        threeLocation = [(405, 355), (513, 441)]
        fourLocation = [(101, 485), (209, 571)]
        fiveLocation = [(253, 485), (361, 571)]
        sixLocation = [(407, 485), (515, 571)]
        sevenLocation = [(101, 615), (209, 701)]
        eightLocation = [(253, 615), (361, 701)]
        nineLocation = [(407, 615), (515, 701)]
        tenLocation = [(101, 745), (209, 831)]
        elevenLocation = [(253, 745), (361, 831)]
        twelveLocation = [(407, 745), (515, 831)]
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。width:  赋值成功::   "+str(tenLocation))
    elif width == '1280' and high == '800':
        oneLocation = [(67, 236), (139, 293)]
        twoLocation = [(168, 236), (240, 293)]
        threeLocation = [(269, 236), (341, 293)]
        fourLocation = [(67, 322), (139, 379)]
        fiveLocation = [(168, 322), (240, 379)]
        sixLocation = [(271, 322), (343, 379)]
        sevenLocation = [(67, 409), (139, 466)]
        eightLocation = [(168, 409), (240, 466)]
        nineLocation = [(271, 409), (343, 466)]
        tenLocation = [(67, 496), (139, 553)]
        elevenLocation = [(168, 496), (240, 553)]
        twelveLocation = [(271, 496), (343, 553)]
    elif width == '1280' and high == '720':
        oneLocation = [(67, 236), (139, 293)]
        twoLocation = [(168, 236), (240, 293)]
        threeLocation = [(269, 236), (341, 293)]
        fourLocation = [(67, 322), (139, 379)]
        fiveLocation = [(168, 322), (240, 379)]
        sixLocation = [(271, 322), (343, 379)]
        sevenLocation = [(67, 409), (139, 466)]
        eightLocation = [(168, 409), (240, 466)]
        nineLocation = [(271, 409), (343, 466)]
        tenLocation = [(67, 496), (139, 553)]
        elevenLocation = [(168, 496), (240, 553)]
        twelveLocation = [(271, 496), (343, 553)]


"""
用于输入法输入管理
"""


class InputManager:



    @staticmethod
    def get_loacation():
        locatio  = eightLocation
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。width:111111111111111  get_loacation：   "+str(locatio))


    @staticmethod
    def find_text_view_by_text(driver, text):
        xpath = "//android.widget.TextView[@text='%s']" % text
        element = driver.find_element_by_xpath(xpath)
        return element

    """
    输入“Delete”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_delete(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        Utils.Logging.info("。。。。。。。。。。。。。。。。。。。width:  get_loacation：   " + str(tenLocation))
        driver.tap(tenLocation, duration)
        time.sleep(after_wait_time)

    """
    输入“Clear”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_clear(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(twelveLocation, duration)
        time.sleep(after_wait_time)

    """
    输入“0”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_zero(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(elevenLocation, duration)
        time.sleep(after_wait_time)

    """
    输入“1”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_one(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(oneLocation, duration)
        time.sleep(after_wait_time)

    """
    输入“2”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_two(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(twoLocation, duration)
        InputManager.find_text_view_by_text(driver, '2').click()
        time.sleep(after_wait_time)

    """
    输入“3”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_three(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(threeLocation, duration)
        InputManager.find_text_view_by_text(driver, '3').click()
        time.sleep(after_wait_time)

    """
    输入“4”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_four(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fourLocation, duration)
        InputManager.find_text_view_by_text(driver, '4').click()
        time.sleep(after_wait_time)

    """
    输入“5”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_five(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fiveLocation, duration)
        InputManager.find_text_view_by_text(driver, '5').click()
        time.sleep(after_wait_time)

    """
    输入“6”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_six(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sixLocation, duration)
        InputManager.find_text_view_by_text(driver, '6').click()
        time.sleep(after_wait_time)

    """
    输入“7”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_seven(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sevenLocation, duration)
        InputManager.find_text_view_by_text(driver, '7').click()
        time.sleep(after_wait_time)

    """
    输入“8”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_eight(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(eightLocation, duration)
        InputManager.find_text_view_by_text(driver, '8').click()
        time.sleep(after_wait_time)

    """
    输入“9”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_nine(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(nineLocation, duration)
        InputManager.find_text_view_by_text(driver, '9').click()
        time.sleep(after_wait_time)

    """
    输入“A”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_a(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(twoLocation, duration)
        InputManager.find_text_view_by_text(driver, 'A').click()
        time.sleep(after_wait_time)

    """
    输入“B”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_b(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(twoLocation, duration)
        InputManager.find_text_view_by_text(driver, 'B').click()
        time.sleep(after_wait_time)

    """
    输入“C”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_c(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(twoLocation, duration)
        InputManager.find_text_view_by_text(driver, 'C').click()
        time.sleep(after_wait_time)

    """
    输入“D”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_d(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(threeLocation, duration)
        InputManager.find_text_view_by_text(driver, 'D').click()
        time.sleep(after_wait_time)

    """
    输入“D”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_e(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(threeLocation, duration)
        InputManager.find_text_view_by_text(driver, 'E').click()
        time.sleep(after_wait_time)

    """
    输入“F”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_f(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(threeLocation, duration)
        InputManager.find_text_view_by_text(driver, 'F').click()
        time.sleep(after_wait_time)

    """
    输入“G”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_g(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fourLocation, duration)
        InputManager.find_text_view_by_text(driver, 'G').click()
        time.sleep(after_wait_time)

    """
    输入“H”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_h(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fourLocation, duration)
        InputManager.find_text_view_by_text(driver, 'H').click()
        time.sleep(after_wait_time)

    """
    输入“I”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_i(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fourLocation, duration)
        InputManager.find_text_view_by_text(driver, 'I').click()
        time.sleep(after_wait_time)

    """
    输入“J”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_j(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fiveLocation, duration)
        InputManager.find_text_view_by_text(driver, 'J').click()
        time.sleep(after_wait_time)

    """
    输入“K”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_k(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fiveLocation, duration)
        InputManager.find_text_view_by_text(driver, 'K').click()
        time.sleep(after_wait_time)

    """
    输入“L”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_l(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fiveLocation, duration)
        InputManager.find_text_view_by_text(driver, 'L').click()
        time.sleep(after_wait_time)

    """
    输入“M”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_m(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sixLocation, duration)
        InputManager.find_text_view_by_text(driver, 'M').click()
        time.sleep(after_wait_time)

    """
    输入“N”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_n(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sixLocation, duration)
        InputManager.find_text_view_by_text(driver, 'N').click()
        time.sleep(after_wait_time)

    """
    输入“O”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_o(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sixLocation, duration)
        InputManager.find_text_view_by_text(driver, 'O').click()
        time.sleep(after_wait_time)

    """
    输入“P”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_p(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sevenLocation, duration)
        InputManager.find_text_view_by_text(driver, 'P').click()
        time.sleep(after_wait_time)

    """
    输入“Q”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_q(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sevenLocation, duration)
        InputManager.find_text_view_by_text(driver, 'Q').click()
        time.sleep(after_wait_time)

    """
    输入“R”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_r(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sevenLocation, duration)
        InputManager.find_text_view_by_text(driver, 'R').click()
        time.sleep(after_wait_time)

    """
    输入“S”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_s(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sevenLocation, duration)
        InputManager.find_text_view_by_text(driver, 'S').click()
        time.sleep(after_wait_time)

    """
    输入“T”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_t(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(eightLocation, duration)
        InputManager.find_text_view_by_text(driver, 'T').click()
        time.sleep(after_wait_time)

    """
    输入“U”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_u(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(eightLocation, duration)
        InputManager.find_text_view_by_text(driver, 'U').click()
        time.sleep(after_wait_time)

    """
    输入“V”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_v(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(eightLocation, duration)
        InputManager.find_text_view_by_text(driver, 'V').click()
        time.sleep(after_wait_time)

    """
    输入“W”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_w(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(nineLocation, duration)
        InputManager.find_text_view_by_text(driver, 'W').click()
        time.sleep(after_wait_time)

    """
    输入“X”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_x(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(nineLocation, duration)
        InputManager.find_text_view_by_text(driver, 'X').click()
        time.sleep(after_wait_time)

    """
    输入“Y”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_y(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(nineLocation, duration)
        InputManager.find_text_view_by_text(driver, 'Y').click()
        time.sleep(after_wait_time)

    """
    输入“Z”，
    duration :点击时长
    before_wait_time: 输入前等待的时长 （默认是2s）
    after_wait_time：输入后等待的时间 （默认是0s）
    """
    @staticmethod
    def input_z(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(nineLocation, duration)
        InputManager.find_text_view_by_text(driver, 'Z').click()
        time.sleep(after_wait_time)



if __name__ == '__main__':
    choose_location_by_device_screen_size(['1920', '1080'])
    InputManager.input_delete()