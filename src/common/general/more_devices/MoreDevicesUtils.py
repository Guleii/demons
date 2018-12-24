from datetime import datetime
import unittest

from general.more_devices.BaseRunner import ParametrizedTestCase
from general.more_devices.BaseStatistics import writeExcel, countDate
from general.more_devices.HomeTest import HomeTest

__author__ = 'Alan'
# -*- coding: utf-8 -*-
"""
多设备并发运行工具类
"""

import os
import random

from general.more_devices.BaseAndroidPhone import getPhoneInfo
from general.more_devices.BaseApk import ApkInfo
from general.more_devices.BaseAppiumServer import AppiumServer
from general.more_devices.BaseInit import mk_file
from multiprocessing import Pool
import config.GlobalConfig as  gl

import sys

sys.path.append("..")
from general.more_devices.BaseAdb import AndroidDebugBridge
import platform

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


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
        # _initApp["systemPort"] = getDevices[i]["systemPort"]

        _initApp["app"] = getDevices[i]["app"]
        apkInfo = ApkInfo(_initApp["app"])
        _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        _initApp["appActivity"] = apkInfo.getApkActivity()
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
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
        # _initApp["systemPort"] = getDevices[i]["systemPort"]

        _initApp["app"] = getDevices[i]["app"]
        apkInfo = ApkInfo(_initApp["app"])
        _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        _initApp["appActivity"] = apkInfo.getApkActivity()
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


def start_run_test_with_more_devices():
    # kill_adb()

    devicess = AndroidDebugBridge().attached_devices()
    if len(devicess) > 0:
        mk_file()
        l_devices = []
        for dev in devicess:
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
        print("没有可用的安卓设备")


if __name__ == '__main__':
    start_run_test_with_more_devices()
