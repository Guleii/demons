import os
from config import globalparameter as gl

"""
    log_tag: 日志过滤条件
    log_level： 日志过滤级别
"""
def log(log_tag='', log_level='E'):
    log_name = gl.report_path+gl.log_name
    if "" == log_tag:
        log_tag = "*"
    cmd = "adb logcat " + " -s " + log_tag + ":" + log_level + " -f >%s" % log_name  # 真正可以过滤的条件
    os.popen(cmd)


def close_log():
    os.system('adb kill-server')

