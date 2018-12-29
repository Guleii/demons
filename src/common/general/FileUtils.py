# coding:utf-8
import os

__author__ = 'Alan'
'''
description:文件操作工具类
'''

"""
判断是否存在文件夹如果不存在则创建为文件夹
"""


def make_dir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")

    else:
        print("---  There is this folder!  ---")