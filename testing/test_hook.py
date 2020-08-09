#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize("a", [1, 0.1, 1000], ids=['整数', '小数', '大数'])
def test_add(a):
    print(a)
    print("case1")


def test_div():
    print("case2")


def test_sub():
    print("case3")


def test_case1(cmdoption):
    print(cmdoption)
