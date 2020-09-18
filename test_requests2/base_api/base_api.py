import requests


class BaseApi:
    ID = "ww93348658d7c66ef4"
    secret = "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"
    def get_token(self):
        r = requests.request(method="get", url= f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.ID}&corpsecret={self.secret}")
        return r.json()