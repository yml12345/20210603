# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：config.py
@时间：2021/5/10  10:46
@文档说明:
"""

import os

path = os.path.realpath(__file__)   #获取该文件所在的路径
DIRE = os.path.dirname(path)  #获取该文件所在的目录
BASE_PATH = os.path.dirname(DIRE) #获取该文件所在的上一层目录
COMMON_PATH = os.path.join(BASE_PATH,"common")
CASES_PATH = os.path.join(BASE_PATH,"cases")
DATAS_PATH = os.path.join(BASE_PATH,"datas")
IMG_PATH = os.path.join(BASE_PATH,"img")
PAGES_PATH = os.path.join(BASE_PATH,"pages")
RESULT_PATH = os.path.join(BASE_PATH,"result")


HOST="http://47.56.240.97:8886/login"