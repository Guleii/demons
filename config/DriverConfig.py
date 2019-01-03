# coding:utf-8


__author__ = 'Helen'
'''
description:driver配置
'''
from general.more_devices.BaseAndroidPhone import *
from appium import webdriver
import config.GlobalConfig as  gl
from general.AdbUtils import ADB
from general.ImageUtils import ImageUtil
from moudle.InputManagerUtils import InputManager
from moudle import InputManagerUtils, HomeTabUtils

"""
    初始化整个项目
"""


def init_all_project_by_device_name(device_name=""):
    init_input_manager_and_tab_location(device_name)


"""
    初始化搜索模块的坐标
"""


def init_input_manager_and_tab_location(device_name):
    current_screen_size_list = ADB(device_name).get_screen_normal_size()
    InputManagerUtils.choose_location_by_device_screen_size(screen_size=current_screen_size_list)
    HomeTabUtils.choose_location_by_device_screen_size(screen_size=current_screen_size_list)
    ImageUtil.choose_location_by_device_screen_size(current_screen_size_list)


class driver_configure():
    # current_connect_device_info = {}

    def get_driver(self):
        """获取driver"""
        try:
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'  # 平台
            # self.desired_caps['platformVersion'] = '8.0.0'  # 系统版本
            # self.desired_caps['platformVersion'] = '6.0'  # 系统版本
            if "" != gl.test_app_path:
                self.desired_caps['app'] = gl.test_app_path  # 测试的app路径
            else:
                self.desired_caps['appPackage'] = gl.test_app_package  # APK包名
                self.desired_caps['appActivity'] = gl.test_app_need_start_splash_activity  # 被测程序启动时的Activity

            # self.desired_caps['app'] = 'E:/autotestingPro/app/UCliulanqi_701.apk'   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
            # self.desired_caps['appPackage'] = 'com.xgimi.home'     # APK包名
            # self.desired_caps['appActivity'] = 'com.xgimi.home.ui.MainActivity'     # 被测程序启动时的Activity

            port = 4723
            device_name ='612QKBQD225A2'


            if gl.test_app_more_devices:
                print("...................................................   "+str(current_connect_device_info))

                port = current_connect_device_info["port"]
                device_name = current_connect_device_info["deviceName"]
                # gl.test_app_more_device_device_name = device_name
                gl.test_app_more_device_device_identity_prefix = get_device_mac(device_name)+"_"
                gl.test_app_more_device_device_name = device_name
                gl.report_name = gl.test_app_more_device_device_identity_prefix + "report.html"
                gl.log_name = gl.test_app_more_device_device_identity_prefix + "Launcher.log"
                self.desired_caps['systemPort'] = current_connect_device_info["systemPort"]
                print("...................................................  qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq   " + gl.test_app_more_device_device_identity_prefix + "   " + device_name + "  mac地址：    ")




            self.desired_caps['unicodeKeyboard'] = False   # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            self.desired_caps['resetKeyboard'] = False  # 是否在测试结束后将键盘重轩为系统默认的输入法。
            self.desired_caps['newCommandTimeout'] = '120'  # Appium服务器等待Appium客户端发送新消息的时间。默认为60秒

            self.desired_caps['deviceName'] = device_name     # 手机类型 一般填写adb devices显示的名称
            self.desired_caps['noReset'] = True  # true:不重新安装APP，false:重新安装app
            # self.desired_caps['automationName'] = 'Uiautomator2' # 用于获取Toast


            remote = "http://127.0.0.1:" + str(port) + "/wd/hub"

            self.driver = webdriver.Remote(remote, self.desired_caps)

            # desired_caps = {}
            # desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = '8.0.0'
            # desired_caps['deviceName'] = '621MECQE3DY4K'
            # desired_caps['noReset'] = True
            # desired_caps['unicodeKeyboard'] = True
            # desired_caps['resetKeyboard'] = True
            # # desired_caps['app'] = 'com.xgimi.instruction30'
            # desired_caps['app'] = 'com.xgimi.home'
            # # desired_caps['appActivity'] = 'com.xgimi.instruction30.net_instruction.ui.SplashActivity'
            # desired_caps['appActivity'] = 'com.xgimi.home.ui.MainActivity'
            # cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            return self.driver
        except Exception as e:
            raise e

    """
        多设备运行前赋值Device信息
    """
    @staticmethod
    def set_device_value(device):
        global current_connect_device_info
        current_connect_device_info = device
        init_all_project_by_device_name(current_connect_device_info["deviceName"])




