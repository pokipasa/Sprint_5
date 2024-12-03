from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


class TestConstructor:
    def test_click_to_constructor(self, driver, login_fixture):

        driver.find_element(By.XPATH, Locators.personal_account_button).click()  # переходим в профиль,
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
        )
        driver.find_element(By.XPATH, Locators.constructor_button).click()  # клик на Конструктор
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_click_to_logotype(self, driver, login_fixture):

        driver.find_element(By.XPATH, Locators.personal_account_button).click()  # переходим в профиль,
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
        )
        driver.find_element(By.XPATH, Locators.logotype_button).click()  # клик на лого
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
