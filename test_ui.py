import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Search_russian import Search_russian
from Pages.search_latin import Search_latin
from Pages.straus_button import Straus_button
from Pages.chat import Chat
from Pages.change_adress import Change_adress


@pytest.fixture
def driver():
    """
           Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    # confirm_adress = driver.find_element(By.ID,'/html/body/script[11]').click()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Ввести в поисковую строку название на кириллице")
@allure.description("Тест проверяет возможность вводить название продуктов, блюд, напитков с использованием кириллицы ")
@allure.feature("Поиск на кириллице")
def test_search_russian(driver):
    search = Search_russian(driver)
    search.seach_russian()


@allure.title("Ввести в поисковую строку валидное значение на латинице")
@allure.feature("Поиск на латинице")
@allure.description("Тест проверяет возможность вводить название продуктов, блюд, напитков с использованием латиницы")
def test_search_latin(driver):
    search = Search_latin(driver)
    search.seach_latin()

@allure.title("Перейти на главную страницу, кликнув на иконку страуса")
@allure.description("Тест проверяет возможность вернуться на главную страницу или обновить главную страницу,"
                    " кликнув на иконку страуса в правом верхнем углу страницы.")
@allure.feature("Главная страница")
def test_straus_button(driver):
    search = Straus_button(driver)
    search.straus_button()

@allure.title("Начать чат с поддержкой")
@allure.description("Тест проверяет возможность быстро в один клик начать час со службой поддержки, "
                    "кликнув на иконку изображения сообщения в левом нижнем углу страницы")
@allure.feature("Чат")
def test_chat(driver):
    button = Chat(driver)
    button.chat()
    assert "Чат с поддержкой" in driver.page_source

@allure.title("Изменить адрес доставки")
@allure.description("Тестируется возможность изменить адрес доставки на этапе выбора продуктов, "
                    "кликнув на окошко с адресом доставки по ценру экрана в верхней части.")
@allure.feature("Адрес доставки")
def test_change_adress(driver):
    adress = Change_adress(driver)
    adress.change_adress()




