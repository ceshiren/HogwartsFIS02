import pytest
import requests

class TestToken:
    @pytest.mark.parametrize("corpid, corpsecret, result",
    [("ww876064acebf0fa3c", "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY", "ok"),
    ("", "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY","corpid missing"),
    ("ww876064acebf0fa3c", "", "corpsecret missing"),
    ("ww876064acebf0fa3", "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY", "invalid corpid")])
    def test_get_token(self, corpid, corpsecret, result):
         '''
         获取 access_token
         '''

         # # 定义凭证
         # corpid = "ww876064acebf0fa3c"
         # corpsecret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

         url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"

         # 发get请求
         r = requests.get(url=url)

         # 打印响应数据
         assert r.json()["errmsg"] == result

    def test_token_param(self):
         '''
         获取token的第二种形式
         '''

         # 定义凭证
         corpid = "ww876064acebf0fa3c"
         corpsecret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

         url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"

         # 定义请求参数
         params = {
              "corpid": corpid,
              "corpsecret": corpsecret
         }

         # 发get请求
         r = requests.get(url=url, params=params)

         # 打印响应
         print(r.json())