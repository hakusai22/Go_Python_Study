import base64
import json
import requests
from Python3_Basis.paypal.authorization import *

# -*- coding: utf-8 -*-
# @Author  : yinpeng
# @Time    : 2024/03/05 13:42

# https://developer.paypal.com/docs/api/orders/v2/#orders_capture

if __name__ == '__main__':

    response = requests.post('https://api.paypal.com/v2/checkout/orders/6G425611J5230925E/capture', headers=get_prod_http_headers())
    print(response.status_code)
    print(response.text)
