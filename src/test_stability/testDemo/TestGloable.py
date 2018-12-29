import sys

import zxing as zxing


from config import DriverConfig
from general.more_devices.BaseAdb import AndroidDebugBridge
from moudle.InputManagerUtils import InputManager
from config import GlobalConfig as gl
from general.ImageUtils import *
from general import QrScanUtils
from src.pages.launcher.vip import VipConfirmPage
from os import path

















def foo():
    global abc
    abc = "hello world"


class AAA:
    @staticmethod
    def bar():
        foo()

    @staticmethod
    def aaa():
        d = path.dirname(__file__)  # 返回当前文件所在的目录
        print(d)
        # print(abc)


class BBB:
    @staticmethod
    def a():
        reader = zxing.BarCodeReader()
        print("......................")
        # barcode = reader.decode("DianZiShuoMingShuErWeiMa.png")
        barcode = reader.decode("sou_hu.png")
        # barcode = reader.decode("Android_AutoTest/test/LaucherTest/screenshot/ai_qi_yi.png")
        # barcode = reader.decode("ai_qi_yi.png")
        # path = r'D:\\Android_AutoTest\\test\\LaucherTest\\screenshot\\ai_qi_yi.png'
        # barcode = reader.decode(path)
        print("搜狐 地址： "+barcode.parsed)

    @staticmethod
    def b():
        reader = zxing.BarCodeReader()
        print("......................")
        # barcode = reader.decode("DianZiShuoMingShuErWeiMa.png")
        barcode = reader.decode("ai_qi_yi.png")
        # barcode = reader.decode("Android_AutoTest/test/LaucherTest/screenshot/ai_qi_yi.png")
        # barcode = reader.decode("ai_qi_yi.png")
        # path = r'D:\\Android_AutoTest\\test\\LaucherTest\\screenshot\\ai_qi_yi.png'
        # barcode = reader.decode(path)
        print("爱奇艺 地址： "+barcode.parsed)

    @staticmethod
    def c():
        reader = zxing.BarCodeReader()
        print("......................")
        # barcode = reader.decode("DianZiShuoMingShuErWeiMa.png")
        barcode = reader.decode("mang_guo.png")
        # barcode = reader.decode("Android_AutoTest/test/LaucherTest/screenshot/ai_qi_yi.png")
        # barcode = reader.decode("ai_qi_yi.png")
        # path = r'D:\\Android_AutoTest\\test\\LaucherTest\\screenshot\\ai_qi_yi.png'
        # barcode = reader.decode(path)
        print("芒果 地址： "+barcode.parsed)


if __name__ == '__main__':
    # VipConfirmPage.test()
    # AAA.aaa()
    # project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))  #返回当前文件所在的目录    # AAA.aaa()
    # d = path.dirname(__file__)
    # d = d+"/screenshot"
    #
    # print(d)
    # forlder = os.path.exists(d)
    # if not forlder:  # 判断是否存在文件夹如果不存在则创建为文件夹
    #     os.makedirs(d)  # makedirs 创建文件时如果路径不存在会创建这个路径
    #     print("---  new folder...  ---")
    #     print("---  OK  ---")
    #
    # else:
    #     print("---  There is this folder!  ---")
    BBB.c()
    BBB.a()
    BBB.b()


    # DriverConfig.init_all_project_by_device_name(AndroidDebugBridge().get_only_one_device_name())
    # InputManager.get_loacation()

