#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

"""
改造1：使用 pytest 测试框架
"""


class TestWeXin:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1  # 等待页面空闲的时间
        # 最重要的一行代码，客户端代码与 Appium Server 建立连接,同时启动起来欢迎页 appActivity
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_send_message(self):
        '''
        录制的脚本：搜索联系人，发送消息
        :return:
        '''
        sendtext = "test003"
        el1 = self.driver.find_element(MobileBy.ID, "gq_")
        el1.click()
        el2 = self.driver.find_element(MobileBy.ID, "ffq")
        el2.send_keys("西西")
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView")
        el3.click()
        el4 = self.driver.find_element(MobileBy.ID, "dtv")
        el4.send_keys(sendtext)
        el5 = self.driver.find_element(MobileBy.ID, "dtr")
        el5.click()
        elements = self.driver.find_elements_by_id("dtg")
        assert sendtext == elements[-1].text

    def test_daka(self):
        '''
        打卡
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        # sleep(3)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gcx").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        result = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/mk").text
        assert "外出打卡成功" == result

    def test_addcontact(self):
        '''
        添加联系人
        :return:
        '''
        name = "hogwarts002"
        gender = "男"
        phonenum = "13600000002"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
            element.click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']").send_keys(
            phonenum)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        # sleep(2)
        # print(self.driver.page_source)
        mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "添加成功" == mytoast
