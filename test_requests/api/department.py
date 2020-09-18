import requests


class Department:

    def create_department(self, token, department_id):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}"
        data = {"name": "葛莱芬多", "name_en": "RDGZ", "parentid": 1, "order": 1, "id": department_id}
        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数
        r = requests.post(url=create_url, json=data)
        return r.json()

    def update_department(self, token ,id):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"
        data = {"id": id, "name": "广州研发中心", "name_en": "RDGZ", "parentid": 1, "order": 1}
        r = requests.post(url=update_url, json=data)
        return r.json()

    def delete_department(self, token, department_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={department_id}"
        r = requests.get(url=delete_url)
        return r.json()

    def get_department_list(self, token):
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}"
        r = requests.get(url=get_department_list_url)
        return r.json()

