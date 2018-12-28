from config import DriverConfig
from general.more_devices.BaseAdb import AndroidDebugBridge
from moudle.InputManagerUtils import InputManager


def foo():
    global abc
    abc = "hello world"


class AAA:
    @staticmethod
    def bar():
        foo()

    @staticmethod
    def aaa():
        print(abc)


class BBB:
    @staticmethod
    def bar():
        AAA.bar()


if __name__ == '__main__':

    # BBB.bar()
    # AAA.aaa()
    DriverConfig.init_all_project_by_device_name(AndroidDebugBridge().get_only_one_device_name())
    InputManager.get_loacation()

