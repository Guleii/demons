# coding:utf-8
__author__ = 'Alan'
'''
description:遥控器按键时间
'''
from appium import webdriver
import time
"""
TV端按键发送工具类
"""


class KeyCode:

    """
       发送遥控器上键事件
       driver: Appium的driver
       wait_time:发送按键之前需要等待时间
       repeat_count:按键重复发送的次数
    """
    @staticmethod
    def touch_up(driver, wait_time=0, repeat_count=1):
        for num in range(0, repeat_count):
            time.sleep(wait_time)
            driver.keyevent(19)


    """
        发送遥控器下键事件
        driver: Appium的driver
        wait_time:发送按键之前需要等待时间
        repeat_count:按键重复发送的次数
    """
    @staticmethod
    def touch_down(driver, wait_time=0, repeat_count=1):
        for num in range(0, repeat_count):
            time.sleep(wait_time)
            driver.keyevent(20)

    """
        发送遥控器左键事件，
        driver: Appium的driver
        wait_time:发送按键之前需要等待时间
        repeat_count:按键重复发送的次数
    """
    @staticmethod
    def touch_left(driver, wait_time=0, repeat_count=1):
        for num in range(0, repeat_count):
            time.sleep(wait_time)
            driver.keyevent(21)
            print("点击了左键")

    """
       发送遥控器右键事件
       driver: Appium的driver
       wait_time:发送按键之前需要等待时间
       repeat_count:按键重复发送的次数
    """
    @staticmethod
    def touch_right(driver, wait_time=0, repeat_count=1):
        for num in range(0, repeat_count):
            time.sleep(wait_time)
            driver.keyevent(22)

    """
        发送遥控器OK键事件
        driver: Appium的driver
        wait_time:发送按键之前需要等待时间
        after_time:发送按键之前后需要等待时间
        repeat_count:按键重复发送的次数
    """
    @staticmethod
    def touch_center(driver, wait_time=0, after_time=0, repeat_count=1):
        for num in range(0, repeat_count):
            time.sleep(wait_time)
            driver.keyevent(23)
            time.sleep(after_time)

    """
           发送遥控器返回键事件
           driver: Appium的driver
           wait_time:发送按键之前需要等待时间
           repeat_count:按键重复发送的次数
     """
    @staticmethod
    def touch_back(driver, wait_time=0, repeat_count=1):
        for num in range(0, repeat_count):
            time.sleep(wait_time)
            driver.keyevent(4)




    """
           发送遥控器Home事件
           driver: Appium的driver
           wait_time:发送按键之前需要等待时间
           repeat_count:按键重复发送的次数
     """
    @staticmethod
    def touch_home(driver, wait_time=0, repeat_count=1):
        for num in range(0, repeat_count):
            time.sleep(wait_time)
            driver.keyevent(3)
