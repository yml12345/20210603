# -*- encoding:utf-8 -*-
"""
@作者：cloveryml
@文件名：base_case.py
@时间：2021/5/10  10:10
@文档说明:
"""

from common.chrome import get_chrome
import pytest
from time import sleep


class BaseCase():
    """测试基类"""


    def setup(self) -> None:
        self.driver = get_chrome()
        sleep(2)



    def teardown(self) -> None:
        self.driver.quit()


