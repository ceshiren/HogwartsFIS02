#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from test_appium.page.member_invite_page import MemberInvitePage
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage


class ContactEditPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    name_element = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']")
    gender_element = (MobileBy.XPATH, "//*[@text='男']")
    female_element = (MobileBy.XPATH, "//*[@text='女']")
    male_element = (MobileBy.XPATH, "//*[@text='男']")
    phonenum_element = (MobileBy.XPATH,
                        "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']")
    save_element = (MobileBy.ID, "com.tencent.wework:id/gq7")

    def edit_name(self, name):
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.find_and_sendkeys(self.name_element, name)
        return self

    def edit_gender(self, gender):

        self.find_and_click(self.gender_element)
        if gender == "女":
            self.find_and_click(self.female_element)
        else:
            self.find_and_click(self.male_element)

        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # if gender == "女":
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # else:
        #     # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        #     sleep(2)
        #     element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
        #     element.click()
        return self

    def edit_phonenum(self, phonenum):
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']").send_keys(
        #     phonenum)
        self.find_and_sendkeys(self.phonenum_element, phonenum)
        return self

    def click_save(self):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        self.find_and_click(self.save_element)
        from test_appium.page.member_invite_page import MemberInvitePage
        return MemberInvitePage(self.driver)
