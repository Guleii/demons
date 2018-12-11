# coding:utf-8
import unittest

__author__ = 'Alan'
'''
description: 单元测试基类
'''

from config import driver_configure
from general.AppLog import *


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver_config = driver_configure.driver_configure()
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
