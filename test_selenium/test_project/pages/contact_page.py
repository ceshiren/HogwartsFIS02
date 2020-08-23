import time

from selenium.webdriver.common.by import By

from test_selenium.test_project.pages.basepage import BasePage


class ContactPage(BasePage):
    _add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _cancel = (By.CSS_SELECTOR, "[node-type='cancel']")

    def go_to_add_member(self):
        # 解决循环导入问题
        from test_selenium.test_project.pages.add_member_page import AddMemberPage
        #todo: 完成点击添加成员操作
        time.sleep(3)
        self.find(*self._add_member).click()

        return AddMemberPage(self.driver)

    def get_member_list(self):
        ele = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        return [name.text for name in ele ]
