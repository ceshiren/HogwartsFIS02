#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def connectDB():
    print("testdemo1下的connectDB")


def test_a(connectDB):
    print("demo1- testa")


class TestA:
    def test_b(self):
        print("demo1.py  testb")
