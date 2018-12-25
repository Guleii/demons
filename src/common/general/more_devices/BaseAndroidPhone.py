
# -*- coding: utf-8 -*-
from general.AdbUtils import ADB

__author__ = 'shikun'
import os
import re
import math
from math import ceil
import subprocess
# 得到手机信息
def getPhoneInfo(devices):
    cmd = "adb -s " + devices +" shell cat /system/build.prop "
    print(cmd)
    # phone_info = os.popen(cmd).readlines()
    phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    result = {"release": "5.0", "model": "model2", "brand": "brand1", "device": "device1"}
    release = "ro.build.version.release=" # 版本
    model = "ro.product.model=" #型号
    brand = "ro.product.brand=" # 品牌
    device = "ro.product.device=" # 设备名
    for line in phone_info:
         for i in line.split():
            temp = i.decode()
            if temp.find(release) >= 0:
                result["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                result["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                result["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                result["device"] = temp[len(device) :]
                break
    print(result)
    return result

# 得到最大运行内存
def get_men_total(devices):
    cmd = "adb -s "+devices+ " shell cat /proc/meminfo"
    get_cmd = os.popen(cmd).readlines()
    men_total = 0
    men_total_str = "MemTotal"
    for line in get_cmd:
        if line.find(men_total_str) >= 0:
            men_total = line[len(men_total_str) +1:].replace("kB", "").strip()
            break
    return int(men_total)
# 得到几核cpu
def get_cpu_kel(devices):
    cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
    get_cmd = os.popen(cmd).readlines()
    find_str = "processor"
    int_cpu = 0
    for line in get_cmd:
        if line.find(find_str) >= 0:
            int_cpu += 1
    return str(int_cpu) + "核"

# 得到手机分辨率
def get_app_pix(devices):
    result = os.popen("adb -s " + devices+ " shell wm size", "r")
    return result.readline().split("Physical size:")[1]


"""
    返回设备的信息
    device_name 连接设备时adb devices 显示的设备名称
"""
def get_device_identity(device_name):
    get_phone = getPhoneInfo(device_name)
    device_identity = get_phone["device"] + "_" + get_phone["brand"] + "_" + get_phone[
        "model"] + "_" + "android" + "_" + get_phone[
                                              "release"]
    return device_identity


def get_device_mac(device_name):
    adb = ADB(device_id=device_name)
    mac = adb.get_mac_address().upper().replace(':', '')
    mac1 = mac[3:15]

    return mac1

if __name__=="__main__":
    getPhoneInfo("DU2TAN15AJ049163")
