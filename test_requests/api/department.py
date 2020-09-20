
from test_requests.api.wework import WeWork


class Department(WeWork):

    def create_department(self,department_id):
        data = {"name": "葛莱芬多", "name_en": "RDGZ", "parentid": 1, "order": 1, "id": department_id}
        req = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}",
            "method": "post",
            "json": data
        }
        r = self.send_requests(req)

        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数

        return r.json()

    def update_department(self, department_id):
        data = {"id": department_id, "name": "广州研发中心", "name_en": "RDGZ", "parentid": 1, "order": 1}
        req = {
            "url":         f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}",
            "method": "post",
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    def delete_department(self, department_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        req = {
            "url": delete_url,
            "method": "get",
        }
        r = self.send_requests(req)

        return r.json()

    def get_department_list(self):
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        req = {
            "url": get_department_list_url,
            "method": "get",
        }
        r = self.send_requests(req)
        return r.json()

