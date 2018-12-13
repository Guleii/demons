# coding:utf-8
__author__ = 'Helen'
'''
description:driver配置
'''
from appium import webdriver


class driver_configure():
    def get_driver(self):
        """获取driver"""
        try:
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'  # 平台
            # self.desired_caps['platformVersion'] = '8.0.0'  # 系统版本
            self.desired_caps['platformVersion'] = '6.0'  # 系统版本
            # self.desired_caps['app'] = 'E:/autotestingPro/app/UCliulanqi_701.apk'   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
            self.desired_caps['appPackage'] = 'com.xgimi.home'     # APK包名
            self.desired_caps['appActivity'] = 'com.xgimi.home.ui.MainActivity'     # 被测程序启动时的Activity
            self.desired_caps['unicodeKeyboard'] = True   # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            self.desired_caps['resetKeyboard'] = True  # 是否在测试结束后将键盘重轩为系统默认的输入法。
            self.desired_caps['newCommandTimeout'] = '120'  # Appium服务器等待Appium客户端发送新消息的时间。默认为60秒
            self.desired_caps['deviceName'] = '612QKBQD225A2'     # 手机ID
            self.desired_caps['noReset'] = True  # true:不重新安装APP，false:重新安装app
            # self.desired_caps['automationName'] = 'Uiautomator2' # 用于获取Toast
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)

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
