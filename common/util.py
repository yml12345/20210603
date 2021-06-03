# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：util.py
@时间：2021/5/22  11:05
@文档说明:
"""
import os,yaml
from common.config import DATAS_PATH
import xlrd

"""读取yaml文件"""
def open_yaml(file):
    filename = os.path.join(DATAS_PATH,file)
    li = []
    with open(filename,"r",encoding="utf-8") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        for i in range(len(data)):

            value = tuple(data[i].values())
            li.append(value)
        return li


a=open_yaml('seckill_new_goods.yaml')
print(a)


def get_data_from_excel(file):
    # filename =os.path.join(DATAS_PATH,file)
    filename = r"D:\Python\DDOU_HD_YML - 副本\datas\login.xlsx"
    #先打开这个excel表格
    li=[]
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)  #打开第一个分页
    a = tuple(table.row_values(1))
    li.append(a)
    return li
#
# a=get_data_from_excel('login.xlsx')
# print(a)