#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 文件名以test_开头， 类名以Test开头， 方法名以test_开头
# 注意：测试类里一定不要加__init__()方法
import pytest
class TestCalc:

    # def setup_class(self):
    #     print("开始计算")
    #     # 实例化计算器
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("结束计算")

    @pytest.mark.add
    def test_add1(self, get_calc, get_datas):
        # # 实例化计算器
        # calc = Calculator()
        # 调用它的相加add() 方法
        result = get_calc.add(get_datas[0], get_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert get_datas[2] == result

    def test_add2(self):
        result = self.calc.add(0.1, 0.2)
        # 断言
        assert 0.3 == round(result, 2)

    @pytest.mark.div
    def test_div(self):
        # # 实例化计算器
        # calc = Calculator()
        r = self.calc.div(1, 1)
        assert 1 == r

    @pytest.mark.div
    def test_div1(self):
        # # 实例化计算器
        # calc = Calculator()
        r = self.calc.div(-1, 1)
        assert -1 == r
