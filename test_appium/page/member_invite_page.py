#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
添加成员页面
'''
# from test_appium.page.contact_edit_page import ContactEditPage
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class MemberInvitePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def addcontact_menual(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmember_element)

        from test_appium.page.contact_edit_page import ContactEditPage
        return ContactEditPage(self.driver)

    def get_toast(self):
        # mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        mytoast = self.gettoast_text()
        return mytoast
