import base64
import json
import requests
from Python3_Basis.paypal.authorization import *

# -*- coding: utf-8 -*-
# @Author  : yinpeng
# @Time    : 2024/02/27 14:29

# https://developer.paypal.com/docs/api/subscriptions/v1/#plans_create
if __name__ == '__main__':

    data1 = {
        "product_id": get_prod_productId(),
        "name": "3 days free trial",
        "description": "3 days free trial",
        "status": "ACTIVE",
        "billing_cycles": [
            {
                "frequency": {
                    "interval_unit": "DAY",
                    "interval_count": 3
                },
                "tenure_type": "TRIAL",
                "sequence": 1,
                "total_cycles": 1,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "0",
                        "currency_code": "USD"
                    }
                }
            },
            {
                "frequency": {
                    "interval_unit": "WEEK",
                    "interval_count": 1
                },
                "tenure_type": "REGULAR",
                "sequence": 2,
                "total_cycles": 0,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "9.99",
                        "currency_code": "USD"
                    }
                }
            }
        ],
        "payment_preferences": {
            "auto_bill_outstanding": True,
            "setup_fee_failure_action": "CONTINUE",
            "payment_failure_threshold": 3
        }
    }

    data2 = {
        "product_id": get_prod_productId(),
        "name": "3 days free trial",
        "description": "3 days free trial",
        "status": "ACTIVE",
        "billing_cycles": [
            {
                "frequency": {
                    "interval_unit": "DAY",
                    "interval_count": 3
                },
                "tenure_type": "TRIAL",
                "sequence": 1,
                "total_cycles": 1,
            },
            {
                "frequency": {
                    "interval_unit": "MONTH",
                    "interval_count": 3
                },
                "tenure_type": "REGULAR",
                "sequence": 2,
                "total_cycles": 0,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "29.99",
                        "currency_code": "USD"
                    }
                }
            }
        ],
        "payment_preferences": {
            "auto_bill_outstanding": True,
            "setup_fee_failure_action": "CONTINUE",
            "payment_failure_threshold": 3
        }
    }

    data3 = {
        "product_id": get_prod_productId(),
        "name": "3 days free trial",
        "description": "3 days free trial",
        "status": "ACTIVE",
        "billing_cycles": [
            {
                "frequency": {
                    "interval_unit": "DAY",
                    "interval_count": 3
                },
                "tenure_type": "TRIAL",
                "sequence": 1,
                "total_cycles": 1,
            },
            {
                "frequency": {
                    "interval_unit": "WEEK",
                    "interval_count": 1
                },
                "tenure_type": "REGULAR",
                "sequence": 2,
                "total_cycles": 0,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "7.49",
                        "currency_code": "USD"
                    }
                }
            }
        ],
        "payment_preferences": {
            "auto_bill_outstanding": True,
            "setup_fee_failure_action": "CONTINUE",
            "payment_failure_threshold": 3
        }
    }

    data4 = {
        "product_id": get_prod_productId(),
        "name": "3 days free trial",
        "description": "3 days free trial",
        "status": "ACTIVE",
        "billing_cycles": [
            {
                "frequency": {
                    "interval_unit": "DAY",
                    "interval_count": 3
                },
                "tenure_type": "TRIAL",
                "sequence": 1,
                "total_cycles": 1,
            },
            {
                "frequency": {
                    "interval_unit": "MONTH",
                    "interval_count": 3
                },
                "tenure_type": "REGULAR",
                "sequence": 2,
                "total_cycles": 0,
                "pricing_scheme": {
                    "fixed_price": {
                        "value": "22.49",
                        "currency_code": "USD"
                    }
                }
            }
        ],
        "payment_preferences": {
            "auto_bill_outstanding": True,
            "setup_fee_failure_action": "CONTINUE",
            "payment_failure_threshold": 3
        }
    }

    response = requests.post('https://api.paypal.com/v1/billing/plans', headers=get_prod_http_headers(), data=json.dumps(data2))
    print(response.status_code)
    print(response.text)


