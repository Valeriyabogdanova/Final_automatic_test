import  requests

BASE_URL = "https://market-delivery.yandex.ru"
#перед тем как запустить автотесты вам необходимо авторизоваться на странице и получить токен
TOKEN = ""

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def test_search_item_positive():
    request = requests.post(f'{BASE_URL}/api/v1/menu/search',
            json={"place_slug":"azbuka_l35f8","text":"арбуз","location":{"lat":59.98401,"lon":30.21288}},
            headers=HEADERS
                             )
    assert request.status_code == 200


def test_put_delivery_adress_positive():
    request = requests.get(f'{BASE_URL}/api/v3/user/addresses/01J57KSFEVCBMYN78R810YR371',
                           headers=HEADERS)

    assert request.status_code == 200

def test_delete_busket():
    request = requests.delete(f'{BASE_URL}'/api/v2/cart?soft_multi=true&longitude=30.21288&latitude=59.98401&screen=checkout&shippingType=delivery&autoTranslate=false&placeSlug=azbuka_l35f8,
                           headers=HEADERS)

    assert request.status_code == 204


def test_empty_json_negative():
    request = requests.post(f'{BASE_URL}/api/v1/menu/search',
                            json={},
                            headers=HEADERS
                            )
    assert request.status_code == 400


def test_wrong_login_negative():
    request = requests.post(f'{BASE_URL}/web-api/passport/profile',
                            json={"uid": "159078888",
                             "login": "user_1",
                            "name": "user_1",
                            "avatar": "2470",
                            "isBetaTester": false,
                            "isYandexEmployee": false"},
                            headers=HEADERS
                            )

    assert request.status_code == 400

