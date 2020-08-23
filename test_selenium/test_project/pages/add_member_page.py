from selenium.webdriver.common.by import By
from test_selenium.test_project.pages.basepage import BasePage
from test_selenium.test_project.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    _username = (By.ID, "username")
    _cancel = (By.CSS_SELECTOR, "[node-type='cancel']")
    def add_member(self, name, acctid, memberAdd_phone):
        #            find_element(By.ID, "username")
        self.find(*self._username).send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(memberAdd_phone)
        # return self 是为了实现返回当前页面时依然可以实现链式调用
        # 相当于 别人调用是， add_member().save_member() 就等同于 self.save_member(self)
        return self

    def save_member(self):
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def cancel_member(self):
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        self.wait_for_clickable(self._cancel)
        self.find(*self._cancel).click()
        return ContactPage(self.driver)



