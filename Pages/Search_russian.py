from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class Search_russian:
    def __init__(self, driver):
        self.driver = driver


    def search_russian(self, word):
        with allure.step("Вход на главную страницу"):
            self.driver.get("https://market-delivery.yandex.ru/moscow?shippingType=delivery")
        with allure.step("Определение поисковой строки по селектору"):
            search_place = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id_1")))
        with allure.step("Ввести в поисковую название продукта на кириллице"):
            return search_place.send_keys(word)
        with allure.step("Поиск по селектору кнопки 'Найти'"):
            search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='UiKitButton_text_c462ced7']"))
        )
        with allure.step("Кликнуть на кнопку 'Найти'"):
            search_button.click()
