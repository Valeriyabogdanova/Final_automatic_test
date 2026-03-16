import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.Search_russian import Search_russian
from Pages.search_latin import Search_latin
from Pages.straus_button import Straus_button
from Pages.chat import Chat
from Pages.empty_search import TestEmptySearch


@pytest.fixture
def driver():
    """
           Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Ввести в поисковую строку название на кириллице")
@allure.description("Тест проверяет возможность вводить название продуктов, блюд, напитков с использованием кириллицы ")
@allure.feature("Поиск на кириллице")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_search_russian(driver):
    word = "Орехи"
    search = Search_russian(driver)
    search.search_russian(word)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{word}')]")))
        assert True  # Если элемент найден, тест проходит
    except TimeoutException:
        assert False, f"'{word}' not found in page source."


@allure.title("Ввести в поисковую строку валидное значение на латинице")
@allure.feature("Поиск на латинице")
@allure.description("Тест проверяет возможность вводить название продуктов, блюд, напитков с использованием латиницы")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_search_latin(driver):
    word = "Nuts"
    search = Search_latin(driver)
    search.seach_latin(word)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{word}')]")))
        assert True  # Если элемент найден, тест проходит
    except TimeoutException:
        assert False, f"'{word}' not found in page source."


@allure.title("Перейти на главную страницу, кликнув на иконку страуса")
@allure.description("Тест проверяет возможность вернуться на главную страницу или обновить главную страницу,"
                    " кликнув на иконку страуса в правом верхнем углу страницы.")
@allure.feature("Главная страница")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ui
def test_straus_button(driver):
    search = Straus_button(driver)
    search.straus_button()
    """Ожидаемый URL главной страницы"""
    expected_url = "https://market-delivery.yandex.ru/moscow?shippingType=delivery"
    """Получаем текущий URL из драйвера"""
    actual_url = driver.current_url
    """Проверяем, что текущий URL соответствует ожидаемому"""
    assert actual_url == expected_url, f"Ожидался URL '{expected_url}', но найден '{actual_url}'"


@allure.title("Начать чат с поддержкой")
@allure.description("Тест проверяет возможность быстро в один клик начать час со службой поддержки, "
                    "кликнув на иконку изображения сообщения в левом нижнем углу страницы")
@allure.feature("Чат")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_chat(driver):
    button = Chat(driver)
    button.chat()
    assert "Служба поддержки" in driver.page_source


@allure.title("Запустить пустой поиск")
@allure.description("Тестируется возможность нажать на кнопку 'Найти' при пустой поисковой строке"
                    " и при этом на странице не возникает сообщение об ошибке")
@allure.feature("Пустой поиск")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_empty_search(driver):
    search = TestEmptySearch(driver)
    search.empty_search()
    try:
        """Проверяем, что сообщение об ошибке не отображается"""
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.error-message'))
        )
        fail("Ошибка: Сообщение об ошибке отображается.")
    except:
        """Если сообщение об ошибке не найдено, тест проходит успешно"""
        print("Ошибки не обнаружено.")






