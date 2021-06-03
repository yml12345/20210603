# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：seckill_activities_set_page.py
@时间：2021/5/24  14:58
@文档说明:秒杀活动设置页面
"""
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SeckillActivitiesSetPage(BasePage):
    #元素定位
    #添加活动
    add_activities_location= (By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[1]/div[7]/button/span")
    tbody_location=(By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[2]/div[3]/table/tbody")
    tr_location = (By.TAG_NAME,"tr")
    td_location = (By.TAG_NAME,"td")
    datetime_location = (By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div")

    def click_add_activities(self):
        self.find_element(self.add_activities_location).click()

    def text_tbody_td_00(self,datetime):
        tbody = self.find_element(self.tbody_location)
        tr_list = self.find_elements(self.tr_location,tbody)
        for tr in tr_list:
            td_list = self.find_elements(self.td_location,tr)
            for td in td_list:
                datetime_text = self.find_element(self.datetime_location,td).text
                if datetime_text == datetime:
                    return datetime_text
