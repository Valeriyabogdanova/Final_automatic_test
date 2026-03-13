from selenium.webdriver.common.by import By

class Change_adress:
    def __init__(self, driver):
        self.driver = driver

    def change_adress(self):
        self.driver.get("https://market-delivery.yandex.ru/moscow?shippingType=delivery")
        adress_place = self.driver.find_element(By.XPATH,
                                           '//*[@id="root"]/div/div/div/header/div/div[1]/div/div[2]/div/button/span/span/span/span[1]')
        adress_place.click()
        next_button = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/div/div/button/div[2]/svg')
        next_button.click()
        clear_button = self.driver.find_element(By.XPATH,
                                           '/html/body/div[4]/div/div/div/div/div[1]/div[2]/div/div/button/svg')
        clear_button.click()
        adress_string = self.driver.find_element(By.XPATH,
                                            '/html/body/div[4]/div/div/div/div/div[1]/div[2]/div/div/div/input')
        adress_string.send_keys("Пушкинская площадь, 2")
        confirm_string = self.driver.find_element(By.XPATH, '//*[@id="react-autowhatever-1--item-0"]/span/div/div[1]')
        confirm_string.click()
        ok_button = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/div[2]/button/span')
        ok_button.click()
