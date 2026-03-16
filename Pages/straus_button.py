from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class Straus_button:
    def __init__(self, driver):
        self.driver = driver

    def straus_button(self):
        with allure.step("Вход на главную страницу"):
            self.driver.get("https://market-delivery.yandex.ru/moscow?shippingType=delivery")
        with allure.step("Определение любой понравившейся иконки по селектору"):
            search_any_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.UiKitSmartImage_cover_e9af3fb2'))
        )
        with allure.step("Кликнуть на эту иконку"):
            search_any_icon.click()
        with allure.step("Определение иконки с изображением страуса по селектору"):
            search_straus = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.rbvr565.c1039e4y'))
        )
        with allure.step("Кликнуть на иконку со страусом"):
            search_straus.click()