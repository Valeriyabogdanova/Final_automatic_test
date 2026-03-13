from selenium.webdriver.common.by import By


class Search_russian:
    def __init__(self, driver):
        self.driver = driver

    def seach_russian(self):
        self.driver.get("https://market-delivery.yandex.ru/moscow?shippingType=delivery")
        search_place = self.driver.find_element(By.CSS_SELECTOR, "[class='i1strjd6 i1jucuro']")
        search_place.send_keys("Орехи")
        search_button = self.driver.find_element(By.CSS_SELECTOR, "[class='i1strjd6 i1jucuro']").click()
