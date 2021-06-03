# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：test_login_case.py
@时间：2021/6/2  9:47
@文档说明:
"""
from cases.base_case import BaseCase
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from time import sleep
from common.util import open_yaml
import pytest,allure
from common.config import DATAS_PATH

class TestLoginCase(BaseCase):
    @allure.story("登录成功-测试用例")
    @pytest.mark.parametrize('username,password',open_yaml('login.yaml'))
    def test_longin(self,username,password):
        with allure.step("进入登录操作"):
            lp = LoginPage(self.driver)
            lp.open()
            sleep(2)
            lp.longin(username,password)
            sleep(2)
        with allure.step("断言"):
            ip = IndexPage(self.driver)
            index_username=ip.text_index_username()
            print(index_username)
            assert username == index_username



#
# if __name__ == '__main__':
#     pytest.main(['-s','test_login_case.py'])