# _*_ coding: utf-8 _*_
__author__ = '54h50m'
__date`__ = '2018/7/9 22:03'

# urllib
# requests

from urllib import request
import requests
# http://t.yushu.im/v2/book/isbn/9787501524044

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text