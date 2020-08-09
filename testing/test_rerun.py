#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pytest


def test_rerun():
    sleep(0.5)
    assert 1 == 2


def test_rerun1():
    sleep(0.5)
    assert 2 == 2


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_rerun2(a):
    sleep(0.5)
    assert 3 == 2
