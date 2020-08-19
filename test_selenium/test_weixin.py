#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo0():
    def setup_method(self, method):
        option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookie(self):
        # get_cookies() 获取当前页面的cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 打开 index页面，这时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 带有登录信息的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851905935585'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851905935585'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325054155915'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'IiwmHmbRQC3UgqmekvGcsqnLM0KaswKi1tpUIxZ7ME4eQqVFuj_8swXg8U3bGeAA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9205189'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629378403.32131, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1597674494,1597732354,1597757140,1597842337'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629378336, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1660914455, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1737553657.1582007476'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597842403'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '9528437336544'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597864124, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8vrdlbn'},
            {'domain': '.qq.com', 'expiry': 1597928855, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1503122815.1597647640'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'qRUzpbH0haAyOoSE7hvpm2vY8YCj94Yxh2h0CFjn4sps63nEtyWRxtWFq3zgA9Ox_oOqrJxdsBGlHIfvmQojMdXEzlaYwzBYb6bdZJLqJAPWwc1ZMBT0EGPYpEkXdqSlgs7cfLUeUrHrW4dDo5yKyequJSMbmefJqVgRVAQjDeytttEwajDTdF-HjpdzDoi1Qv377KsOSGSM6hITMWleJsZgBqxnXlFHF6NG3gd44jwN-_ayhvINXvBFrx-vS94xEjMkyu5oVq2_8qfY_NKUwQ'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600434633, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'en-us%2Cen'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 重新打开 已带有cookie 信息的index 页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def test_importcontact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 带有登录信息的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851905935585'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851905935585'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325054155915'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'IiwmHmbRQC3UgqmekvGcsqnLM0KaswKi1tpUIxZ7ME4eQqVFuj_8swXg8U3bGeAA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9205189'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629378403.32131, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1597674494,1597732354,1597757140,1597842337'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629378336, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1660914455, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1737553657.1582007476'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597842403'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '9528437336544'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597864124, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8vrdlbn'},
            {'domain': '.qq.com', 'expiry': 1597928855, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1503122815.1597647640'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'qRUzpbH0haAyOoSE7hvpm2vY8YCj94Yxh2h0CFjn4sps63nEtyWRxtWFq3zgA9Ox_oOqrJxdsBGlHIfvmQojMdXEzlaYwzBYb6bdZJLqJAPWwc1ZMBT0EGPYpEkXdqSlgs7cfLUeUrHrW4dDo5yKyequJSMbmefJqVgRVAQjDeytttEwajDTdF-HjpdzDoi1Qv377KsOSGSM6hITMWleJsZgBqxnXlFHF6NG3gd44jwN-_ayhvINXvBFrx-vS94xEjMkyu5oVq2_8qfY_NKUwQ'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600434633, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'en-us%2Cen'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 重新打开 已带有cookie 信息的index 页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("/Users/juanxu/Downloads/mydata.xlsx")
        assert "mydata.xlsx" == self.driver.find_element(By.ID, "upload_file_name").text

    # 实现 cookie 数据的持久化存储
    def test_shelve(self):
        # shelve python 内置的模块，相当于小型的数据库
        # 带有登录信息的cookie
        db = shelve.open('./mydbs/cookies')
        # db['cookie'] = cookies
        # db.close()
        cookies = db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 重新打开 已带有cookie 信息的index 页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("/Users/juanxu/Downloads/mydata.xlsx")
        assert "mydata.xlsx" == self.driver.find_element(By.ID, "upload_file_name").text
