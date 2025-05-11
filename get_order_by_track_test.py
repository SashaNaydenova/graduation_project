# Александра Найденова, 29-я когорта — Финальный проект. Инженер по тестированию плюс


import sender_stand_request
import configuration
import requests
import data


def test_get_order_by_track():
    track_number = sender_stand_request.get_new_order_track()
    response = sender_stand_request.get_order_by_track(track_number)
    assert response.status_code == 200
