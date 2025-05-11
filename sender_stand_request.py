import configuration
import requests
import data


def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


def get_new_order_track():
    response = post_create_order(data.order_body)
    response_data = response.json()
    track = response_data.get('track')
    return track


def get_order_by_track(track_number):
    response = requests.get(
        configuration.URL_SERVICE +
        configuration.GET_ORDER_BY_NUMBER + str(track_number)
    )
    return response
