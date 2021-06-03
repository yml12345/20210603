# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：chrome.py
@时间：2021/5/10  10:16
@文档说明:
"""
from selenium import webdriver

def get_chrome():
    drive = webdriver.Chrome()
    drive.maximize_window()
    drive.implicitly_wait(30)
    return drive

