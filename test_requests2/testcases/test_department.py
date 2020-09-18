# -*- coding: utf-8 -*-
# @Time    : 2020-09-16 21:24
# @Author  : feier
# @File    : test_departments.py
import requests
from jsonpath import jsonpath


class TestDepartments:

    def setup_class(self):
        '''
        获取token
        '''
        # 定义凭证
        token = requests.session()
        r = token.request(method="get", url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                          params={"corpid": "ww93348658d7c66ef4",
                                  "corpsecret": "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"})

        # 获取token
        self.token = r.json()["access_token"]


    def test_create_department(self):
        '''
        创建部门
        '''
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"

        # 定义请求参数
        param = {"access_token": self.token}

        # 定义请求体
        data = {"name": "技术部123456789123456789123456789", "name_en": "tech department", "parentid": 1, "order": 1,
            "id": 2}

        # 发post请求
        r = requests.post(url=url, json=data, params=param)

        # 打印响应
        get_list = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        getlist = requests.get(url=get_list)
        # 断言
        # 查询
        assert getlist.json()["department"][1]["name"] == "技术部123456789123456789123456789"
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "created"
    def test_update_department(self):
        update_list = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {"name": "技术部", "name_en": "tech department", "parentid": 1, "order": 1,
            "id": 2}
        # proxy = {"http": "http://127.0.0.1:8888", "https":"http://127.0.0.1:8888"}
        r = requests.post(url=update_list, json=data)


        get_list = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        getlist = requests.get(url=get_list)


    def test_delete_department(self):

        """
        删除部门
        :return:
        """
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=2"
        requests.get(url= delete_url)
        get_list = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        getlist = requests.get(url=get_list)
        name = jsonpath(getlist.json(), "$..id")
        print("name是",name)
        assert 2 not in name
