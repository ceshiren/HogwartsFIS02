import json

import yaml

from test_requests.api.department import Department


class TestDeparment():

    def setup_class(self):
        self.deparment = Department()
        config_infor = yaml.safe_load(open("config.yaml"))
        # 通过传入不同的secret获取不同的token权限，给不同的业务测试用例使用。
        # 当secret 和业务紧密相关， 应该抽离出来维护
        self.deparment.get_token(config_infor["token"]["department_secret"])

    def test_department(self):
        self.deparment.create_department(3)
        list = self.deparment.get_department_list()
        name = self.deparment.base_jsonpath(list, "$..name")
        assert "葛莱芬多" in name

    def test_update_department(self):
        self.deparment.update_department(3)
        list = self.deparment.get_department_list()
        name = self.deparment.base_jsonpath(list, "$..name")
        assert "广州研发中心" in name


    def test_delete_department(self):
        ## 删除id 为3 的部门
        self.deparment.delete_department(3)
        # 获取部门所有的信息
        list = self.deparment.get_department_list()
        # 使用jsonpath，提取出，所有的部门id
        department_id = self.deparment.base_jsonpath(list, "$..id")
        assert 3 not in department_id

        # assert len(list["department"]) == 1

    def test_get_department_list(self):
        r = self.deparment.get_department_list()
        get_list_schema = json.load(open("./json_schema/get_list_schema.json"))
        self.deparment.base_jsonschema(r, get_list_schema)


