#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
通讯录页面
'''
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.member_invite_page import MemberInvitePage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_text = "添加成员"

    def add_memeber(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_by_scroll_and_click(self.addmember_text)
        return MemberInvitePage(self.driver)
