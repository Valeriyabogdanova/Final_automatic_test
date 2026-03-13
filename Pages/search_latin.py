from selenium.webdriver.common.by import By
import allure

class Search_latin:
    def __init__(self, driver):
        self.driver = driver

    def seach_latin(self):
        with allure.step("Вход на главную страницу"):
            self.driver.get("https://market-delivery.yandex.ru/moscow?shippingType=delivery")
        with allure.step("Определение поисковой строки по селектору"):
            search_place = self.driver.find_element(By.CSS_SELECTOR, "[class='i1strjd6 i1jucuro']")
        with allure.step("Ввести в поисковую название продукта на латинице"):
            search_place.send_keys("Nuts")
        with allure.step("Кликнуть на кнопку 'Найти'"):
            search_button = self.driver.find_element(By.CSS_SELECTOR, "[class='i1strjd6 i1jucuro']").click()