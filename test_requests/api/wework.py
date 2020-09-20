
from test_requests.api.baseapi import BaseApi


class WeWork(BaseApi):

    def get_token(self, corp_secret):
        """
        token的定义
        """
        corp_id = "ww93348658d7c66ef4"
        # corp_secret = "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"
        # get_token 的请求信息
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"}
        # token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        # r = requests.get(url=token_url)
        r = self.send_requests(req)
        self.token = r.json()["access_token"]
        return self.token
