# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：seckill_activities_set.py
@时间：2021/5/24  14:49
@文档说明:
"""
import os,ddt,unittest
from time import sleep
from cases.base_case import BaseCase
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.seckill_and_free.seckill_activities_set_page import SeckillActivitiesSetPage
from pages.seckill_and_free.add_goods_page import AddGoodsPage
from pages.seckill_and_free.add_seckill_goods_page import AddSeckillGoodsPage

from common.config import DATAS_PATH


@ddt.ddt
class SeckillActivitiesSetCase(BaseCase):

    @ddt.file_data(os.path.join(DATAS_PATH,"add_seckill_goods.yaml"))
    def test_new_goods_seckill_Package_mail(self, **case):
        """福利秒杀或品牌中心，包邮"""
        img = case.get("img")
        username = case.get("username")
        password = case.get("password")
        datetime = case.get("datetime")
        goods_name = case.get("goods_name")
        inventory_number = case.get("inventory_number")
        false_inventory_number = case.get("false_inventory_number")
        print(img)
        # 登录页面
        lp = LoginPage(self.driver)
        lp.open()
        sleep(2)
        lp.longin(username, password)
        sleep(2)
        # 主页面
        ip = IndexPage(self.driver)
        #点击 秒杀和免费领 菜单
        ip.click_index_seckill_and_free()
        sleep(1)
        #点击 秒杀活动设置 菜单
        ip.click_index_seckill_activities_set()
        sleep(1)
        #进入秒杀活动设置页面
        sap = SeckillActivitiesSetPage(self.driver)
        sap.click_add_activities()
        #进入添加福利秒杀商品页面
        asgp = AddSeckillGoodsPage(self.driver)
        #选择日期信息
        asgp.send_choose_time(datetime)
        #点击 选择商品
        asgp.click_choose_goods()
        #进入 添加商品 列表页面
        agp = AddGoodsPage(self.driver)
        #勾选需要添加的商品
        agp.click_chooose_more_goods(goods_name)
        sleep(1)
        #并点击 确定 按钮
        agp.click_determine()
        sleep(1)
        #输入 库存 信息
        asgp.send_inventory(inventory_number)
        #输入 假库存 信息
        asgp.send_false_inventory(false_inventory_number)
        #并保存
        asgp.click_save()
        sleep(1)
        #断言
        datetime01=sap.text_tbody_td_00(datetime)
        self.assertEqual(datetime,datetime01)






if __name__ == '__main__':
    unittest.main()