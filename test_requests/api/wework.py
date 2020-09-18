import requests


class WeWork():

    def get_token(self):
        """
        token的定义
        """
        corp_id = "ww93348658d7c66ef4"
        corp_secret = "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        return r.json()["access_token"]