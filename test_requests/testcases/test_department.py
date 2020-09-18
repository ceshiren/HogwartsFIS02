from test_requests.api.department import Department
from test_requests.api.wework import WeWork


class TestDeparment():

    def setup_class(self):
        wework = WeWork()
        self.deparment = Department()
        self.token = wework.get_token()

    def test_department(self):
        self.deparment.create_department(self.token, 3)
        list = self.deparment.get_department_list(self.token)
        assert list["department"][1]["name"] == "葛莱芬多"

    def test_update_department(self):
        self.deparment.update_department(self.token, 3)
        list = self.deparment.get_department_list(self.token)
        print(list)
        assert list["department"][1]["name"] == "广州研发中心"


    def test_delete_department(self):
        self.deparment.delete_department(self.token, 3)
        list = self.deparment.get_department_list(self.token)
        print(list)
        assert len(list["department"]) == 1

    def test_get_department_list(self):
        self.deparment.get_department_list(self.token)

