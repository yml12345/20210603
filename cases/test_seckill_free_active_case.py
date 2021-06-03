# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：test_seckill_free_active_case.py
@时间：2021/6/2  11:37
@文档说明:
"""
from cases.base_case import BaseCase
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.seckill_and_free.seckill_free_active_page import SeckillFreeActivePage
from pages.seckill_and_free.new_goods_page import NewGoodsPage
from time import sleep
import os
import pytest
from common.mysql import delete_mysql
from common.util import open_yaml
import allure

@allure.feature('添加活动商品功能流程测试')
class TestSeckillFreeActiveCase(BaseCase):

    @pytest.mark.parametrize('img,username,password,order_num,goods_name,goods_img,activity_name,package_mail,postage,market_price,seckill_price,vip_price,all_png,details_img',open_yaml("free_new_goods.yaml"))
    @allure.story("免费领或商品兑换券，并不包邮")
    def test_new_goods_free_not_Package_mail(self,img,username,password,order_num,goods_name,goods_img,activity_name,package_mail,postage,market_price,seckill_price,vip_price,all_png,details_img):
        """免费领或商品兑换券，并不包邮"""
        print(img)
        #登录页面
        with allure.step("先进行登录操作"):
            lp = LoginPage(self.driver)
            lp.open()
            sleep(2)
            lp.longin(username,password)
            sleep(2)
        with allure.step("点击主页中的【秒杀和免费领】菜单"):
        #主页面
            ip = IndexPage(self.driver)
            ip.click_index_seckill_and_free()
            sleep(2)
        with allure.step("再点击【活动商品管理】菜单"):
            ip.click_index_active_goods()
            sleep(1)
        # #活动商品管理页面
        with allure.step("进入活动商品管理页面，获取该页面商品的条数"):
            scfp = SeckillFreeActivePage(self.driver)
            scfp.click_active_new_goods()
            sleep(2)
            #获取该页面商品的条数
            total01_num=scfp.text_total_num()
            print(total01_num)
        with allure.step("点击【新建商品】页面，进行添加商品操作"):
            ngp = NewGoodsPage(self.driver)
            ngp.send_order_by(order_num)
            sleep(2)
            ngp.send_goods_name(goods_name)
            sleep(2)
            ngp.click_goods_img()
            sleep(4)
            os.system(goods_img)
            sleep(1)
            ngp.click_activity_type(activity_name)
            sleep(1)
            ngp.click_package_mail(package_mail)
            sleep(1)
            ngp.send_the_postage(postage)
            sleep(1)
            ngp.send_the_market_price(market_price)
            sleep(1)
            ngp.send_the_seckill_price(seckill_price)
            sleep(1)
            ngp.send_the_vip_price(vip_price)
            sleep(2)
            all_png = all_png
            for i in all_png:
                ngp.click_graphic_details()
                sleep(2)
                os.system(details_img % i)
                sleep(2)
            ngp.click_determine()
            sleep(4)
        with allure.step("统计添加活动商品后，该列表页面的商品条数"):
            total02_num=scfp.text_total_num()
            print(total02_num)
        with allure.step("断言"):
            assert total01_num != total02_num
        # try:
        #     delete_mysql(sql,goods_name)
        # except Exception:
        #     print("不执行该删除语句")

    @pytest.mark.parametrize('img,username,password,order_num,goods_name,goods_img,activity_name,higher_return,vip_return,package_mail,default,market_price,seckill_price,vip_price,all_png,details_img',open_yaml("seckill_new_goods.yaml"))
    @allure.story("福利秒杀或品牌中心，包邮")
    def test_new_goods_seckill_Package_mail(self,img,username,password,order_num,goods_name,goods_img,activity_name,higher_return,vip_return,package_mail,default,market_price,seckill_price,vip_price,all_png,details_img):
        """福利秒杀或品牌中心，包邮"""
        print(img)
        with allure.step("先进行登录操作"):
            lp = LoginPage(self.driver)
            lp.open()
            sleep(2)
            lp.longin(username, password)
            sleep(2)
        with allure.step("点击主页中的【秒杀和免费领】菜单"):
            ip = IndexPage(self.driver)
            ip.click_index_seckill_and_free()
            sleep(2)
        with allure.step("再点击【活动商品管理】菜单"):
            ip.click_index_active_goods()
            sleep(1)
        with allure.step("进入活动商品管理页面，获取该页面商品的条数"):
            scfp = SeckillFreeActivePage(self.driver)
            scfp.click_active_new_goods()
            sleep(2)
            total01_num = scfp.text_total_num()
            print(total01_num)
        with allure.step("点击【新建商品】页面，进行添加商品操作"):
            ngp = NewGoodsPage(self.driver)
            ngp.send_order_by(order_num)
            sleep(2)
            ngp.send_goods_name(goods_name)
            sleep(2)
            ngp.click_goods_img()
            sleep(4)
            os.system(goods_img)
            sleep(1)
            ngp.click_activity_type(activity_name)
            sleep(1)
            ngp.send_the_higher_return(higher_return)
            ngp.send_vip_return(vip_return)
            sleep(1)
            ngp.click_package_mail(package_mail)
            sleep(1)
            ngp.send_the_market_price(market_price,default=default)
            sleep(1)
            ngp.send_the_seckill_price(seckill_price,default=default)
            sleep(1)
            ngp.send_the_vip_price(vip_price,default=default)
            sleep(2)
            all_png = all_png
            for i in all_png:
                ngp.click_graphic_details(default=default)
                sleep(2)
                os.system(details_img % i)
                sleep(2)
            ngp.click_determine()
            sleep(4)
        with allure.step("统计添加活动商品后，该列表页面的商品条数"):
            total02_num = scfp.text_total_num()
            print(total02_num)
        with allure.step("断言"):
            assert total01_num != total02_num
    #     # try:
    #     #     delete_mysql(sql, goods_name)
    #     # except Exception:
    #     #     print("不执行该删除语句")



#
# if __name__ == '__main__':
#     pytest.main(['-s','test_seckill_free_active_case.py','--alluredir','result'])
#     os.system('allure generate ./result -o ./report --clean')