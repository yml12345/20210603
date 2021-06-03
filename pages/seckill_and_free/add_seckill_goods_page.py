# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：add_seckill_goods_page.py
@时间：2021/5/24  16:57
@文档说明:添加福利秒杀商品页面
"""
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AddSeckillGoodsPage(BasePage):
    #元素定位
    choose_time_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div:nth-child(4) > div > div.el-dialog__body > form > div.item-wrapper > div.el-form-item.is-required.el-form-item--small > div > div > input")
    choose_goods_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div:nth-child(4) > div > div.el-dialog__body > form > div.format-item-wrapper > div:nth-child(1) > div:nth-child(1) > button > span")
    #库存输入框
    inventory_location = (By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[2]/div[4]/div[2]/div[2]/div/div/input")
    #假库存输入框
    false_inventory_location = (By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[2]/div[5]/div[1]/div[2]/div/div/input")
    #保存按钮
    save_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div:nth-child(4) > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small > span")



    #元素对应的操作方法
    def send_choose_time(self,datetime):
        """选择 日期"""
        return self.find_element(self.choose_time_location).send_keys(datetime)

    def click_choose_goods(self):
        """点击 选择商品  """
        self.find_element(self.choose_goods_location).click()

    def send_inventory(self,inventory_number):
        """填写  库存 信息"""
        return self.find_element(self.inventory_location).send_keys(inventory_number)

    def send_false_inventory(self,false_inventory_number):
        """填写 假库存 信息"""
        return self.find_element(self.false_inventory_location).send_keys(false_inventory_number)


    def click_save(self):
        """点击 保存  按钮"""
        self.find_element(self.save_location).click()