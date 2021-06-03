# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：add_goods_page.py
@时间：2021/5/24  16:59
@文档说明:添加商品页面
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddGoodsPage(BasePage):
    #元素定位
    #页面列表
    tbody_location = (By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[2]/div[3]/table/tbody")
    tr_location = (By.TAG_NAME,"tr")
    td_location = (By.TAG_NAME,"td")
    choose_location= (By.TAG_NAME,"td>div>label>span> span")

    #确定按钮
    determine_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div:nth-child(5) > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small > span")

    #相应元素的操作
    def click_chooose_more_goods(self,goods_name):
        """勾选满足条件的商品"""
        tbody = self.find_element(self.tbody_location)
        print(tbody)
        tr_list = self.find_elements(self.tr_location,tbody)
        print(len(tr_list),tr_list)
        for tr in tr_list:
            td_list = self.find_elements(self.td_location,tr)
            print(len(td_list), td_list)
            if td_list[2].text == goods_name:
                self.find_element(self.choose_location,td_list[0]).click()

    def click_determine(self):
        self.find_element(self.determine_location).click()