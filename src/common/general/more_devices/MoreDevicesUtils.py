
# -*- coding: utf-8 -*-
__author__ = 'Alan'
"""
多设备并发运行工具类
"""


from datetime import datetime
import unittest

from general.more_devices.BaseRunner import ParametrizedTestCase
from general.more_devices.BaseStatistics import writeExcel, countDate
from general.more_devices.HomeTest import HomeTest
from config import DriverConfig
from src.suite.RunTest import run_case_more_devices



import os
import random

from general.more_devices.BaseAndroidPhone import getPhoneInfo
from general.more_devices.BaseApk import ApkInfo
from general.more_devices.BaseAppiumServer import AppiumServer
from general.more_devices.BaseInit import mk_file
from multiprocessing import Pool
import config.GlobalConfig as gl

import sys

sys.path.append("..")
from general.more_devices.BaseAdb import AndroidDebugBridge
import platform

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

appium_first_port = 4800    # appium的启动的第一个设备端口
appium_first_bport = 4750  # appium启动的bootstrap-port端口
appium_first_systemPort = 4750  # appium启动的systemPort端口 注意以上desired_caps参数为必加参数，其他参数参照官方文档。这里重点说下systemPort参数，由于在android7.0及以上设备中有些控件appium不能识别，故加上此参数，此时appium会自动安装两个apk（基于uiautomator2.0）。






"""
重启adb
"""
def kill_adb():
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system(PATH("../app/kill5037.bat"))
    else:
        os.popen("killall adb")
    os.system("adb start-server")


def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices)) #加入测试类
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")


def runnerPool(getDevices):
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        # _initApp["automationName"] = "uiautomator2"
        _initApp["systemPort"] = getDevices[i]["systemPort"]

        _initApp["app"] = getDevices[i]["app"]
        # apkInfo = ApkInfo(_initApp["app"])
        # _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        # _initApp["appActivity"] = apkInfo.getApkActivity()
        _initApp["appPackage"] = "com.xgimi.zhushou"
        _initApp["appActivity"] = "com.xgimi.zhushou.alan.ui.SplashActivity"
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    pool.map(run_test_case, devices_Pool)
    pool.close()
    pool.join()


"""
给定固定测试应用的名称以及启动界面的名称
"""


def runnerPoolByGivenDeviceInfo(getDevices):
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        # _initApp["automationName"] = "uiautomator2"
        _initApp["systemPort"] = getDevices[i]["systemPort"]


        # _initApp["app"] = getDevices[i]["app"]
        # apkInfo = ApkInfo(_initApp["app"])
        # _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        # _initApp["appActivity"] = apkInfo.getApkActivity()
        # _initApp["appPackage"] = "com.xgimi.zhushou"
        # _initApp["appActivity"] = "com.xgimi.zhushou.alan.ui.SplashActivity"
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    # pool.map(run_case_more_devices, devices_Pool)
    pool.map(run_test_case, devices_Pool)
    pool.close()
    pool.join()


"""
启动多设备连接的测试--demo
"""
def start_run_test_with_more_devices():
    # kill_adb()

    devices = AndroidDebugBridge().attached_devices()
    if len(devices) > 0:
        mk_file()
        l_devices = []
        for dev in devices:
            app = {}
            app["devices"] = dev
            app["port"] = str(random.randint(4700, 4900))
            app["bport"] = str(random.randint(4700, 4900))
            app["systemPort"] = str(random.randint(4700, 4900))
            app["app"] = PATH(gl.project_path + "/app/WuPingZhuShou4.0.4_Oppo.apk")  # 测试的app路径,喜马拉雅app

            l_devices.append(app)

        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runnerPool(l_devices)
        writeExcel()
        appium_server.stop_server(l_devices)
    else:
        raise Exception("没有可用的安卓设备")
        print("没有可用的安卓设备")


"""
启动多设备连接的测试
"""


def start_run_test_with_more_devices_with_accurate():
    # kill_adb()

    devices = AndroidDebugBridge().attached_devices()
    if len(devices) > 0:
        mk_file()
        l_devices = []
        for dev in devices:
            index = devices.index(dev)
            add_count = index*10
            app = {}
            app["devices"] = dev
            # app["port"] = str(appium_first_port+add_count)
            # app["bport"] = str(appium_first_bport+add_count)
            # app["systemPort"] = str(appium_first_systemPort+add_count)

            app["port"] = str(random.randint(4700, 4900))
            app["bport"] = str(random.randint(4700, 4900))
            app["systemPort"] = str(random.randint(4700, 4900))


            if "" != gl.test_app_path:
                app["app"] = gl.test_app_path  # 测试的app路径

            l_devices.append(app)

        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runnerPoolByGivenDeviceInfo(l_devices)
        # runnerPool(l_devices)
        # writeExcel()
        appium_server.stop_server(l_devices)
    else:
        raise Exception("没有可用的安卓设备")
        print("没有可用的安卓设备")



def run_test_case(devices):
    DriverConfig.driver_configure.set_device_value(devices)
    run_case_more_devices()
    # testDemo(devices)


def testDemo(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices)) #加入测试类
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")


if __name__ == '__main__':
    start_run_test_with_more_devices()
    # start_run_test_with_more_devices_with_accurate()