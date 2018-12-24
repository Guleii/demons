import re

__author__ = 'shikun'
from math import floor
import subprocess
import os
import json
'''
apk文件的读取信息
'''
class ApkInfo():
    def __init__(self, apkPath):
        self.apkPath = apkPath

# 得到app的文件大小
    def getApkSize(self):
        size = floor(os.path.getsize(self.apkPath) / (1024 * 1000))
        return str(size) + "M"


    def getApkBaseInfo(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        bt = b'\xb2\xbb\xca\xc7\xc4\xda\xb2\xbf\xbb\xf2\xcd\xe2\xb2\xbf\xc3\xfc\xc1\xee\xa3\xac\xd2\xb2\xb2\xbb\xca\xc7\xbf\xc9\xd4\xcb\xd0\xd0\xb5\xc4\xb3\xcc\xd0\xf2\r\n\xbb\xf2\xc5\xfa\xb4\xa6\xc0\xed\xce\xc4\xbc\xfe\xa1\xa3\r\n'
        print("获取的apk信息。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。                  "+str(output.decode('GBK'))+"                       err:  "+str(err.decode('GBK')))
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)

        print('packagename:' + packagename)
        print('versionCode:' + versionCode)
        print('versionName:' + versionName)
        return packagename, versionName, versionCode

    #得到应用名字
    def getApkName(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        t = output.decode().split()
        for item in t:
            # print(item)
            match = re.compile("application-label:(\S+)").search(item)
            if match is not None:
                return match.group(1)


    #得到启动类

    def getApkActivity(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        print("=====getApkActivity=========")
        match = re.compile("launchable-activity: name=(\S+)").search(output.decode())
        print("match=%s" %match)
        if match is not None:
            return match.group(1)
if __name__ == '__main__':
    pass
    # ApkInfo(r"D:\app\appium\Img\Jianshu-2.3.1.apk").getApkActivity()
    # ApkInfo(r"D:\app\appium\Img\Jianshu-2.3.1.apk").getApkActivity()
    # # ApkInfo(r"D:\app\appium_study\Img\t.apk").get_apk_version()
    # # ApkInfo(r"D:\app\appium_study\Img\t.apk").get_apk_name()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()
    # ApkInfo(r"D:\app\appium_study\Img\t.apk").get_apk_activity()


