__author__ = 'Alan'
# -*- coding: utf-8 -*-
import subprocess
import re, os
import math
# 常用的性能监控
def top_cpu(devices, pkg_name):
    cmd = "adb -s "+devices+" shell dumpsys cpuinfo | grep -w " + pkg_name+":"
    get_cmd = os.popen(cmd).readlines()
    for info in get_cmd:
        return float(info.split()[2].split("%")[0])



# 得到men的使用情况
def get_men(devices, pkg_name):
    cmd = "adb -s "+devices+" shell  dumpsys  meminfo %s"  %(pkg_name)
    total = "TOTAL"
    get_cmd = os.popen(cmd).readlines()
    for info in get_cmd:
        info_sp = info.strip().split()
        for item in range(len(info_sp)):
            if info_sp[item] == total:
               return int(info_sp[item+1])
    return 0

# 得到fps
def get_fps(devices, pkg_name):
    print("fps-")
    _adb = "adb -s "+devices+" shell dumpsys gfxinfo %s | grep -A 128 'Execute'  | grep -v '[a-Z]' "%pkg_name
    result = os.popen(_adb).read().strip()
    result = result.split('\r\n')
    # r_result = [] # 总值
    # t_result = [] # draw,Process,Execute分别的值
    # f_sum = 0
    for i in result:
        l_result = i.split('\t')[-3:]
        f_sum = 0
        for j in l_result:
            r = re.search(r"\d+\.\d+", str(j))
            if r:
                f_sum += float(r.group())
            # t_result.append('%.2f'%f_sum)
        return float('%.2f'%f_sum)
