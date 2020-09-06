#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
app.py 存放app一些特有的操作
比如：启动应用， 关闭应用，重启应用，进入到首页
"""
from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main_page import MainPage


class App(BasePage):
    def start(self):
        '''
        启动app
        :return:
        '''
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps['settings[waitForIdleTimeout]'] = 1  # 等待页面空闲的时间
            # 最重要的一行代码，客户端代码与 Appium Server 建立连接,同时启动起来欢迎页 appActivity
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 隐式等待
            self.driver.implicitly_wait(5)
        else:
            # launch_app() 启动 desirecap 里面设置的appActivity
            # self.driver.start_activity(appPackage, appActivity) 可以启动任何应用
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        '''
        跳转到首页
        :return:
        '''
        return MainPage(self.driver)
