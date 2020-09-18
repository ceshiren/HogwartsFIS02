# 创建部门成功 -> 更新部门成功 -> 删除部门
import requests


class TestDepartment:
    def setup_class(self):
        corp_id = "ww93348658d7c66ef4"
        corp_secret = "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        self.token = r.json()["access_token"]
        self.id  = 2


    def test_create_department(self):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
               "name": "葛莱芬多",
               "name_en": "RDGZ",
               "parentid": 1,
               "order": 1,
               "id": self.id
            }
        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数
        r = requests.post(url=create_url, json= data)
        ## 调用查询部门列表接口，获取部门列表信息
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url= get_department_list_url)
        ## 通过得到查询部门列表接口的返回值， 实现查看部门是否新建成功
        assert list.json()["department"][1]["name"] == "葛莱芬多"
        assert r.json()["errmsg"] == 'created'

    def test_update_department(self):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
               "id": self.id,
               "name": "广州研发中心",
               "name_en": "RDGZ",
               "parentid": 1,
               "order": 1
            }
        requests.post(url= update_url, json= data)
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url= get_department_list_url)
        print(list.json())
        assert list.json()["department"][1]["name"] == "广州研发中心"

    def test_delete_department(self):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.id}"
        requests.get(url=delete_url)
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url)
        assert len(list.json()["department"]) == 1