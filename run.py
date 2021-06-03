# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：run.py
@时间：2021/5/10  10:10
@文档说明:
"""
import pytest,os
from common.config import RESULT_PATH,CASES_PATH

if __name__ == '__main__':
    pytest.main(['-s', CASES_PATH, '--alluredir', RESULT_PATH])
    os.system('allure generate ./result -o ./report --clean')
