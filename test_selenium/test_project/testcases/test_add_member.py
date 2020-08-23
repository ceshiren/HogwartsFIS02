from test_selenium.test_project.pages.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()


    def test_add_member(self):
        # 1. 从首页跳转到添加成员页面 2. 添加成员
        namelist = self.main.go_to_add_member().add_member("ez","555","13899990000").save_member().get_member_list()
        assert "ez" in namelist

    def test_add_member_fail(self):
        namelist = self.main.go_to_add_member().add_member("ez2","555","13899990000").cancel_member().get_member_list()
        assert "ez2" not in namelist


    def test_contact_member(self):
        self.main = MainPage()
        self.main.go_to_contact().go_to_add_member().add_member("ez2","5553","18899990000").save_member().get_member_list()

    def teardown(self):
        self.main.driver.quit()