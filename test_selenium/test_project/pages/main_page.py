from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_selenium.test_project.pages.add_member_page import AddMemberPage
from test_selenium.test_project.pages.basepage import BasePage
from test_selenium.test_project.pages.contact_page import ContactPage

class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _add_member = (By.CSS_SELECTOR, "[node-type='addmember']")
    _menu_contacts = (By.ID, "menu_contacts")
    def go_to_contact(self):
        # 对contactpage 类进行实例化，表示业务逻辑的转换关系
        self.find(*self._menu_contacts).click()
        return ContactPage(self.driver)

    def go_to_add_member(self):
        self.find(*self._add_member).click()
        # 第二次初始化， 子类AddMemberPage初始化
        return AddMemberPage(self.driver)
