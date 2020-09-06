#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
主页：
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.addresslist_page import AddressListPage
from test_appium.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addresslist(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find(self.addresslist_element).click()
        return AddressListPage(self.driver)

    def goto_workbench(self):
        pass
