#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_a():
    print("test_demo.py  测试用例a")


def test_b():
    print("test_demo.py  测试用例b")


def test_c():
    assert 1 == 2


def test_d():
    assert 100 == 200


def test_e():
    assert 100 == 200


@pytest.mark.parametrize('a', [1, 2, 3, 0])
@pytest.mark.parametrize('b', [4, 5, 6, 7])
def test_param(a, b):
    print(f"a = {a} , b = {b}")
