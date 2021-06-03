# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：mysql.py
@时间：2021/5/22  14:51
@文档说明:连接数据库
"""
import pymysql


config = {
    'host': '47.56.240.97',
    'port':5506,
    'user':'ddou',
    'password':'Renmai@2020',
    'db':'dcep_share',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor
}


def select_mysql(sql):
    db = pymysql.connect(**config)
    cur = db.cursor()
    cur.execute(sql)
    data= cur.fetchall()
    db.close()
    return data



def delete_mysql(sql,goods_name):
    db = pymysql.connect(**config)
    cur = db.cursor()
    cur.execute(sql,goods_name)
    db.commit()
    db.close()

sql = 'DELETE from dcep_share.ec_goods where goods_name=%s;'


delete_mysql('DELETE from dcep_share.ec_goods where goods_name=%s;','测试商品002')

