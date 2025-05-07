# Александра Найденова, 29-я когорта — Финальный проект. Инженер по тестированию плюс


import sender_stand_request
import configuration
import requests
import data 

def test_get_order_by_track():
    track = sender_stand_request.get_new_order_track()
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER + str(track))

response=test_get_order_by_track()
assert response.status_code == 200