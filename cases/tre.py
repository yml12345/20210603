# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：tre.py
@时间：2021/5/20  17:21
@文档说明:
"""
from selenium import webdriver
import os
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://47.56.240.97:8886/")
# 用户名输入框
driver.find_element_by_css_selector("#app > div > div > form > div:nth-child(1) > div > div > input").send_keys("yml")
time.sleep(2)
# 密码输入框
driver.find_element_by_css_selector("#app > div > div > form > div:nth-child(2) > div > div > input").send_keys("123456")
time.sleep(2)
# 登录按钮
driver.find_element_by_css_selector("#app > div > div > form > div.login-btn > button").click()
time.sleep(2)
# 秒杀和免费领
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/ul/li[4]/div/span").click()
time.sleep(2)
# 活动商品管理
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/ul/li[4]/ul/li[3]").click()
time.sleep(2)
# “新建商品” 按钮
driver.find_element_by_css_selector("#app > div > div.content-box > div.content > div > div:nth-child(1) > div:nth-child(7) > button").click()
time.sleep(2)
# 排序
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[1]/div/div/input").send_keys("1")
time.sleep(2)
# 商品名称
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[2]/div/div/input").send_keys("测试商品1")
time.sleep(2)
# 商品图片
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[3]/div/div/div/i").click()
time.sleep(2)
os.system("D:\\abc.exe")
time.sleep(4)
# 图文详情
all_png = ["D:\工作\图片\\1dd9e81d6a924d98bb04a99966bc8435bbocll.jpg","D:\工作\图片\\3bbd67a9395241f4b36f4cefe3e9612098777e.gif","D:\工作\图片\\1dd9e81d6a924d98bb04a99966bc8435bbocll.jpg","D:\工作\图片\\3bbd67a9395241f4b36f4cefe3e9612098777e.gif"]
for i in all_png:
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[10]/div/div/div/i").click()
    time.sleep(3)
    print(i)
    os.system("D:\\abcd.exe %s" % i)
    time.sleep(3)
