import time

from selenium.webdriver.common.by import By

from test_selenium.test_project.pages.basepage import BasePage


class ContactPage(BasePage):
    _add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _cancel = (By.CSS_SELECTOR, ".js_btn_cancel")

    def go_to_add_member(self):
        # 解决循环导入问题
        from test_selenium.test_project.pages.add_member_page import AddMemberPage
        # 确认添加成员按钮是可点的
        self.wait_for_clickable(self._add_member)
        # 进入死循环
        while True:
            self.find(*self._add_member).click()
            # 报错被捕获，执行except循环点击找元素操作，直到找到为主
            try:
                # 找到添加成员页面的某个元素
                res = self.find(*self._cancel)
                # 如果存在的话就跳出循环，如果不存在的话，就报错
                if res is not None:
                    break
            except:
                print("暂时没找到")
        return AddMemberPage(self.driver)

    def get_member_list(self):
        ele = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        return [name.text for name in ele ]
