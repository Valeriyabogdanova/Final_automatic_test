from selenium.webdriver.common.by import By
import allure

class Chat:
    def __init__(self, driver):
        self.driver = driver

    def chat(self):
        with allure.step("Вход на главную страницу"):
            self.driver.get("https://market-delivery.yandex.ru/moscow?shippingType=delivery")
        with allure.step("Поиск по селектору на кнопки 'Чат'"):
            start_button = self.driver.find_element(By.XPATH, '//button[@title="Служба поддержки"]')
        with allure.step("Кликнуть на кнопку 'ЧАт'"):
            start_button.click()