import requests
import allure
from asyncio.windows_events import NULL
import pytest


BASE_URL = "https://market-delivery.yandex.ru"

#перед тем как запустить автотесты вам необходимо авторизоваться на странице и получить session_id в разделе  application/cookie

HEADERS = {
    "Cookie": "Session_id=3:1773403238.5.0.1773137736314:rAb8bQ:2266.1.2:1|2345812358.0.2.3:1773137736|3:11774471.461335.ELtUmw5jFCVb450c7lEemKHo0vc",
    "Content-Type": "application/json"
}

@allure.title("Запрос на поиск продукта в поисковой строке на кириллице")
@allure.feature("Поиск")
@allure.description("Тест позволяет посылать определенные апи-запросы и сравнивать полученный результат с ожидаемым")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_search_item_positive():
    search_word = "молоко"

    response = requests.post(f'{BASE_URL}/api/v1/menu/search',
                             json={
        "place_slug": "pyaterochka_nhowv",
        "text": search_word,
         "block_type": "user_search_history",
         "location": {
        "lat": 55.767098724886154,
        "lon": 37.602552528500524
         }
            },
                             headers=HEADERS
                             )
    assert response.status_code == 200
    assert search_word in response.text


@allure.title("Запрос на адрес доставки")
@allure.feature("Адрес")
@allure.description("Тест позволяет посылать апи-запросы на отображение адреса доставки и сравнивать полученный результат с ожидаемым")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_put_delivery_address_positive():
    response = requests.get(f'{BASE_URL}/api/v3/user/addresses',
                            headers=HEADERS)
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Проверяем, что ответ - это список адресов


@allure.title("Запрос на поиск с пустым json")
@allure.feature("Невалидное тело запроса")
@allure.description("Тест позволяет посылать апи-запросы с некорректным пустым json в теле и ожидаемо получать ошибку в ответе")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_empty_json_negative():
    response = requests.post(f'{BASE_URL}/api/v1/menu/search',
                             json={},
                             headers=HEADERS
                             )
    assert response.status_code == 400


@allure.title("Запрос с неверным паролем")
@allure.feature("Невалидный пароль")
@allure.description("Тест позволяет посылать апи-запросы с некорректным паролем в теле и ожидаемо получать ошибку в ответе")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_wrong_login_negative():
    response = requests.post(f'{BASE_URL}/web-api/passport/profile',
                             json={
                                 "uid": "159078888",
                                 "login": "user_1",
                                 "name": "user_1",
                                 "avatar": "2470",
                                 "isBetaTester": False,
                                 "isYandexEmployee": False
                             },
                             headers=HEADERS
                             )

    assert response.status_code == 200


@allure.title("Запрос с некорректным телом")
@allure.feature("Некорректное тело запроса")
@allure.description("Тест позволяет посылать апи-запросы на поиск товаров c полем, не допускающим значение 'NULL'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_not_null():
    response = requests.post(f'{BASE_URL}/api/v1/menu/search',
                             json={"place_slug": NULL,"text":"чай","location":{"lat":59.98401,"lon":30.21288}},
                             headers=HEADERS
                                 )
    assert response.status_code == 400

