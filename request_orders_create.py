import configuration
import requests
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         headers=data.headers,
                         json=data.order_body)



