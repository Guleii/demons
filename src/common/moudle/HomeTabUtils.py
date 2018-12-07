# coding:utf-8
__author__ = 'Alan'
'''
description: Launcher主界面点击Tab栏法的工具类
'''


import time

oneLocation = [(102, 123), (223, 165)]
twoLocation = [(216, 123), (366, 165)]
threeLocation = [(366, 123), (516, 165)]
fourLocation = [(516, 123), (650, 165)]
fiveLocation = [(650, 123), (800, 165)]
sixLocation = [(800, 123), (950, 165)]
sevenLocation = [(950, 123), (1136, 165)]
eightLocation = [(1136, 123), (1286, 165)]
nineLocation = [(1286, 123), (1436, 165)]
tenLocation = [(1436, 123), (1557, 165)]
elevenLocation = [(1557, 123), (1707, 165)]


# 点击某一个点击Tab栏前默认的等待的时间
defaultWaitTime = 3
# 点击某一个点击Tab栏后默认的等待的时间
defaultAfterWaitTime = 0


class TabUtils:

    """
    点击Tab栏“1”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_one(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(oneLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“2”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_two(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(twoLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“3”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_three(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(threeLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“4”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_four(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fourLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“5”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_five(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(fiveLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“6”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_six(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sixLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“7”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_seven(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(sevenLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“8”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_eight(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(eightLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“9”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_nine(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(nineLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“10”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_ten(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(tenLocation, duration)
        time.sleep(after_wait_time)

    """
    点击Tab栏“11”，
    duration :点击时长
    before_wait_time: 点击Tab栏前等待的时长 （默认是2s）
    after_wait_time：点击Tab栏后等待的时间 （默认是0s）
    """
    @staticmethod
    def click_tab_eleven(driver, duration=100, before_wait_time=defaultWaitTime, after_wait_time=defaultAfterWaitTime):
        time.sleep(before_wait_time)
        driver.tap(elevenLocation, duration)
        time.sleep(after_wait_time)

