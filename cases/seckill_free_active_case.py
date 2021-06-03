# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：seckill_free_active_case.py
@时间：2021/5/10  14:01
@文档说明:
"""
from cases.base_case import BaseCase
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.seckill_and_free.seckill_free_active_page import SeckillFreeActivePage
from pages.seckill_and_free.new_goods_page import NewGoodsPage
from time import sleep
import os,ddt
import unittest
from common.config import DATAS_PATH
from common.mysql import delete_mysql


@ddt.ddt
class LoginCase(BaseCase):

    @ddt.file_data(os.path.join(DATAS_PATH,"free_new_goods.yaml"))
    @unittest.skip
    def test_new_goods_free_not_Package_mail(self,**case):
        """免费领或商品兑换券，并不包邮"""

        username = case.get("username")
        password = case.get("password")
        order_num = case.get("order_num")
        goods_img = case.get("goods_img")
        goods_name = case.get("goods_name")
        activity_name = case.get("activity_name")
        package_mail = case.get("package_mail")
        postage = case.get("postage")
        market_price = case.get("market_price")
        seckill_price = case.get("seckill_price")
        vip_price = case.get("vip_price")
        all_png = case.get("all_png")
        details_img = case.get("details_img")
        sql = case.get("sql")
        #登录页面
        lp = LoginPage(self.driver)
        lp.open()
        sleep(2)
        lp.longin(username,password)
        sleep(2)
        #主页面
        ip = IndexPage(self.driver)
        ip.click_index_seckill_and_free()
        sleep(2)
        ip.click_index_active_goods()
        sleep(1)
        #活动商品管理页面
        scfp = SeckillFreeActivePage(self.driver)
        scfp.click_active_new_goods()
        sleep(2)
        #获取该页面商品的条数
        total01_num=scfp.text_total_num()
        print(total01_num)
        #新建商品页面
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
        total02_num=scfp.text_total_num()
        print(total02_num)
        self.assertNotEqual(total01_num,total02_num)
        try:
            delete_mysql(sql,goods_name)
        except Exception:
            print("不执行该删除语句")

    @ddt.file_data(os.path.join(DATAS_PATH, "seckill_new_goods.yaml"))
    def test_new_goods_seckill_Package_mail(self, **case):
        """福利秒杀或品牌中心，包邮"""
        img = case.get("img")
        username = case.get("username")
        password = case.get("password")
        order_num = case.get("order_num")
        goods_img = case.get("goods_img")
        goods_name = case.get("goods_name")
        activity_name = case.get("activity_name")
        higher_return = case.get("higher_return")
        vip_return = case.get("vip_return")
        package_mail = case.get("package_mail")
        postage = case.get("postage")
        default = case.get("default")
        market_price = case.get("market_price")
        seckill_price = case.get("seckill_price")
        vip_price = case.get("vip_price")
        all_png = case.get("all_png")
        details_img = case.get("details_img")
        sql = case.get("sql")
        print(img)
        # 登录页面
        lp = LoginPage(self.driver)
        lp.open()
        sleep(2)
        lp.longin(username, password)
        sleep(2)
        # 主页面
        ip = IndexPage(self.driver)
        ip.click_index_seckill_and_free()
        sleep(2)
        ip.click_index_active_goods()
        sleep(1)
        # 活动商品管理页面
        scfp = SeckillFreeActivePage(self.driver)
        scfp.click_active_new_goods()
        sleep(2)
        # 获取该页面商品的条数
        total01_num = scfp.text_total_num()
        print(total01_num)
        # 新建商品页面
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
        try:
            ngp.send_the_higher_return(higher_return)
            ngp.send_vip_return(vip_return)
        except Exception:
            print("未获取到上级返豆信息和VIP返豆信息，不执行该语句")
        sleep(1)
        ngp.click_package_mail(package_mail)
        sleep(1)
        try:
            ngp.send_the_postage(postage)
        except Exception:
            print("未获取到邮费字段信息，不执行该语句")
        if default:
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
        else:
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
        total02_num = scfp.text_total_num()
        print(total02_num)
        self.assertNotEqual(total01_num, total02_num)
        # try:
        #     delete_mysql(sql, goods_name)
        # except Exception:
        #     print("不执行该删除语句")




if __name__ == '__main__':
    unittest.main()