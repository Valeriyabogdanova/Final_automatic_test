from selenium.webdriver.common.by import By

class Chat:
    def __init__(self, driver):
        self.driver = driver

    def chat(self):
        self.driver.get("https://market-delivery.yandex.ru/moscow?shippingType=delivery")
        start_button = self.driver.find_element(By.XPATH, '//button[@title="Служба поддержки"]')
        start_button.click()