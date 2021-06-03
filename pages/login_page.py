# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：login_page.py
@时间：2021/5/10  11:02
@文档说明:登录页面
"""
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    """登录页面元素定位"""
    #用户名输入框
    username_location = (By.CSS_SELECTOR,"#app > div > div > form > div:nth-child(1) > div > div > input")
    #密码输入框
    password_location = (By.CSS_SELECTOR,"#app > div > div > form > div:nth-child(2) > div > div > input")
    #登录按钮
    longin_location = (By.CSS_SELECTOR,"#app > div > div > form > div.login-btn > button")

    def send_username(self,username):
        """输入用户名"""
        return self.find_element(self.username_location).send_keys(username)

    def send_password(self,password):
        """输入密码"""
        return self.find_element(self.password_location).send_keys(password)

    def click_login(self):
        """点击 登录 按钮"""
        self.find_element(self.longin_location).click()

    def longin(self,username,password):
        """登录操作"""
        self.send_username(username)
        self.send_password(password)
        self.click_login()
