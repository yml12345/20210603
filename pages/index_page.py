# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：index_page.py
@时间：2021/5/10  11:45
@文档说明:主页面
"""
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class IndexPage(BasePage):
    """主页面元素定位"""
    #用户名元素
    index_username_location = (By.CSS_SELECTOR,"#app > div > div.header > div.header-right > div > div.user-name.el-dropdown > span")
    #秒杀和免费领
    index_seckill_and_free_location = (By.XPATH,"//*[@id=\"app\"]/div/div[2]/ul/li[4]/div/span")
    #秒杀活动设置
    index_seckill_activities_set_location = (By.XPATH,"//*[@id=\"app\"]/div/div[2]/ul/li[4]/ul/li[1]")
    #活动商品管理
    index_active_goods_location = (By.XPATH,"//*[@id=\"app\"]/div/div[2]/ul/li[4]/ul/li[3]")

    """元素操作"""
    def text_index_username(self):
        """获取该页面的 用户名"""
        return self.find_element(self.index_username_location).text

    def click_index_seckill_and_free(self):
        """点击 秒杀和免费领 菜单"""
        self.find_element(self.index_seckill_and_free_location).click()

    def click_index_seckill_activities_set(self):
        """点击 秒杀活动设置 菜单"""
        self.find_element(self.index_seckill_activities_set_location).click()

    def click_index_active_goods(self):
        """点击 活动商品管理 菜单"""
        self.find_element(self.index_active_goods_location).click()
