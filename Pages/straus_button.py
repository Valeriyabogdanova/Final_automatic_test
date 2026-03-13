from selenium.webdriver.common.by import By

class Straus_button:
    def __init__(self, driver):
        self.driver = driver

    def straus_button(self):
        self.driver.get("https://market-delivery.yandex.ru/moscow?shippingType=delivery")
        search_any_icon = self.driver.find_element(By.CSS_SELECTOR,'[class="UiKitSmartImage_cover_e9af3fb2"]')
        search_any_icon.click()
        search_straus = self.driver.find_element(By.CSS_SELECTOR,"[class='rbvr565 c1039e4y']").click()
        search_straus.click()