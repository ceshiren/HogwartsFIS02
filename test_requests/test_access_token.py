import pytest
import requests


class TestToken:
    # 前面定义的是参数的名称， 后面定义的是参数具体的值， 以[(),()]
    @pytest.mark.parametrize(
        "corp_id, corp_secret, errmsg",
        [("ww93348658d7c66ef4","T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw","ok"),
         ("","T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw", "corpid missing"),
         ("ww93348658d7c66ef4","", "corpsecret missing")])
    # 在定义方法的时候， 需要定义出来pytest装饰器中定义的形参
    def test_token(self, corp_id, corp_secret, errmsg):
        # corp_id = "ww93348658d7c66ef4"
        # corp_secret = "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url= token_url)
        print(r.json())
        # # 校验corpsecret必填逻辑是否生效
        assert r.json()["errmsg"] == errmsg
