# coding:utf-8
import unittest

from general import Utils
from general.AdbUtils import ADB
from general.more_devices.BaseAdb import AndroidDebugBridge
from moudle import InputManagerUtils

__author__ = 'Alan'
'''
description: 单元测试基类
'''

from config import DriverConfig
from general.AppLog import *


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Utils.Logging.debug("；；；；；；；；；；；；；；；；；；；；；；；；；Launcher稳定性测试111111111111")
        # DriverConfig.init_all_project_by_device_name(AndroidDebugBridge().get_only_one_device_name())
        # current_screen_size_list = ADB(AndroidDebugBridge().get_only_one_device_name()).get_screen_normal_size()
        # InputManagerUtils.choose_location_by_device_screen_size(screen_size=current_screen_size_list)


        driver_config = DriverConfig.driver_configure()
        cls.driver = driver_config.get_driver()
        log()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # closeLog()

    def add_img(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass
