# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：base_page.py
@时间：2021/5/10  11:00
@文档说明:
"""
from common.config import HOST
class BasePage():

    def __init__(self,driver,url=HOST):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    #元素定位
    def find_element(self,location,element=None):
        if element:
            return element.find_element(*location)
        else:
            return self.driver.find_element(*location)

    def find_elements(self,location,element=None):
        if element:
            return element.find_elements(*location)
        else:
            return self.driver.find_elements(*location)