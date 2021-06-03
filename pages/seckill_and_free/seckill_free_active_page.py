# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：seckill_free_active_page.py
@时间：2021/5/10  14:30
@文档说明:活动商品管理页面
"""
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SeckillFreeActivePage(BasePage):
    """元素定位"""
    #“新建商品” 按钮
    active_new_goods_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div:nth-child(1) > div:nth-child(7) > button")
    #商品列表
    table_location = (By.TAG_NAME,"table")
    tr_location = (By.TAG_NAME,"tr")
    td_location = (By.TAG_NAME,"td")
    #统计条数
    total_num_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div:nth-child(1) > div.el-pagination.is-background > span")

    """元素操作"""
    def click_active_new_goods(self):
        self.find_element(self.active_new_goods_location).click()


    def count_table_num(self):
        table = self.find_element(self.table_location)
        tr_list = self.find_elements(self.tr_location,table)
        a = len(tr_list)
        for tr in tr_list:
            td_list = self.find_elements(self.td_location,tr)

    def text_total_num(self):
        return self.find_element(self.total_num_location).text
