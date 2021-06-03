# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：new_goods_page.py
@时间：2021/5/10  14:40
@文档说明:新建商品页面
"""
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class NewGoodsPage(BasePage):
    """元素定位"""
    #排序
    order_by_location = (By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[1]/div/div/input")
    #商品名称
    goods_name_location = (By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[2]/div/div/input")
    #商品图片
    goods_img_location=(By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[3]/div/div/div/i")
    #活动类型
    form_dive_04_div_element_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div")
    activity_type_label_elements_location = (By.TAG_NAME,"label")
    activity_type_label_span_elements_location = (By.CSS_SELECTOR,"label>span")
    activity_type_label_span_span_elements_location = (By.CSS_SELECTOR, "label>span>span") #活动类型对应的选择框
    #上级返D豆
    the_higher_return_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div > div > input")
    #vip返豆
    vip_return_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(6) > div > div > input")
    #是否包邮（福利秒杀或品牌中心）
    seckill_form_dive_07_div_element_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(7) > div")
    #是否包邮(免费领或商品兑换券)
    free_form_dive_05_div_element_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div")
    package_mail_label_elements_location = (By.TAG_NAME,"label")
    package_mail_label_span_elements_location = (By.CSS_SELECTOR,"label>span")
    package_mail_label_span_span_elements_location = (By.CSS_SELECTOR, "label>span>span") #活动类型对应的选择框
    #邮费
    the_postage_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(6) > div > div > input")
    #市场价（福利秒杀、品牌中心）
    seckill_the_market_price_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div > div > input")
    #市场价（免费领、商品兑换券）
    free_the_market_price_location=(By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(7) > div > div > input")
    #福利价（福利秒杀、品牌中心）
    seckill_the_seckill_price_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(9) > div > div > input")
    #福利价（免费领、商品兑换券）
    free_the_seckill_price_location=(By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div > div > input")
    # VIP价（福利秒杀、品牌中心）
    seckill_vip_price_location = (By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(10) > div > div > input")
    #VIP价（免费领、商品兑换券）
    free_the_vip_price_location=(By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(9) > div > div > input")
    #规格
    #图文详情（福利秒杀、品牌中心）
    seckill_graphic_details_location=(By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[12]/div/div/div/i")
    #图文详情（免费领、商品兑换券）
    free_graphic_details_location=(By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[11]/div/div/div/i")

    #确定按钮
    determine_location =(By.CSS_SELECTOR,"#app > div > div.content-box > div.content > div > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small > span")

    """元素操作"""
    def send_order_by(self,order_num):
        """输入排序信息"""
        return self.find_element(self.order_by_location).send_keys(order_num)

    def send_goods_name(self,goods_name):
        """输入商品名称"""
        return self.find_element(self.goods_name_location).send_keys(goods_name)

    def click_goods_img(self):
        """点击商品图片，进行图片上传"""
        self.find_element(self.goods_img_location).click()

    def click_activity_type(self,activity_name):
        """选择活动类型"""
        #对第四个div标签进行元素定位
        div_element = self.find_element(self.form_dive_04_div_element_location)
        print(div_element)
        #获取第四个div标签下的所有label标签
        label_list = self.find_elements(self.activity_type_label_elements_location,div_element)
        print(len(label_list),label_list)
        #对所有label标签进行循环，并找到对应每个label标签的所有span标签
        for label in label_list:
            span_list = self.find_elements(self.activity_type_label_span_elements_location,label)
            print(len(span_list),span_list)
            for span in span_list:
                if span.text == activity_name:
                    self.find_element(self.activity_type_label_span_span_elements_location,span_list[0]).click()


    def send_the_higher_return(self,higher_return):
        """填写上级返后字段信息"""
        return self.find_element(self.the_higher_return_location).send_keys(higher_return)


    def send_vip_return(self,vip_return):
        """填写VIP返豆信息"""
        return self.find_element(self.vip_return_location).send_keys(vip_return)




    def click_package_mail(self,package_mail,default=None):
        """选择是否包邮"""
        if default:
            div_element = self.find_element(self.seckill_form_dive_07_div_element_location)
        else:
            div_element = self.find_element(self.free_form_dive_05_div_element_location)
        label_list = self.find_elements(self.package_mail_label_elements_location,div_element)
        for label in label_list:
            span_list = self.find_elements(self.package_mail_label_span_elements_location,label)
            for span in span_list:
                if span.text == package_mail:
                    self.find_element(self.package_mail_label_span_span_elements_location,span_list[0]).click()


    def send_the_postage(self,postage):
        """填写邮费信息"""
        return self.find_element(self.the_postage_location).send_keys(postage)


    def send_the_market_price(self,market_price,default=None):
        """输入市场价信息"""
        if default:
            return self.find_element(self.seckill_the_market_price_location).send_keys(market_price)
        else:
            return self.find_element(self.free_the_market_price_location).send_keys(market_price)


    def send_the_seckill_price(self,seckill_price,default=None):
        """输入福利价"""
        if  default:
            return self.find_element(self.seckill_the_seckill_price_location).send_keys(seckill_price)
        else:
            return self.find_element(self.free_the_seckill_price_location).send_keys(seckill_price)

    def send_the_vip_price(self,vip_price,default=None):
        """输入VIP价格"""
        if default:
            return self.find_element(self.seckill_vip_price_location).send_keys(vip_price)
        else:
            return self.find_element(self.free_the_vip_price_location).send_keys(vip_price)


    def click_graphic_details(self,default=None):
        """点击图文详情，进行图片上传"""
        if default:
            self.find_element(self.seckill_graphic_details_location).click()
        else:
            self.find_element(self.free_graphic_details_location).click()

    def click_determine(self):
        """点击确定按钮"""
        self.find_element(self.determine_location).click()