# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：long.py
@时间：2021/5/22  10:17
@文档说明:
"""

from pages.login_page import LoginPage
from pages.index_page import IndexPage
from time import sleep
import unittest
from common.chrome import get_chrome
import ddt,os
from common.config import DATAS_PATH
from common.util import open_yaml
class Login():

    login = open_yaml("login.yaml")
    username = login.get("username")
    password = login.get("password")

    def base_login(self):
        lp = LoginPage(get_chrome())
        lp.open()
        sleep(2)
        lp.longin(self.username,self.password)
        sleep(2)
