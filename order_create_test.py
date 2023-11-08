# Кирилл Поздеев, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import request_orders_create
import data

def save_order_track_number():
    responce_new_order = request_orders_create.post_new_order()
    get_order_track_number = responce_new_order.json()["track"]
    return get_order_track_number


def get_order_by_track_number():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACKNUMBER + str(save_order_track_number()),
                         headers=data.headers)


def test_chek_number_status_code():
    assert get_order_by_track_number().status_code == 200