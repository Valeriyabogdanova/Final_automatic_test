import pytest
from selenium import webdriver
import allure


@pytest.fixture(scope="session")
def driver():
    with allure.step("Открыть и настроить браузер"):
        timeout = 10

        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(timeout)
        driver.maximize_window()
        yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()