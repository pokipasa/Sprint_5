import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from test_data import TestData

login = f'testtestov{random.randint(1000, 99999)}@yandex.ru'
password = [
    random.choice(string.ascii_lowercase + string.digits if i != 5 else string.ascii_uppercase) for i in range(10)
]


class TestHomeWork:

    def test_sign_in_successful(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, Locators.name_input).send_keys("FredricBackman")
        driver.find_element(By.XPATH, Locators.email_input).send_keys(login)
        driver.find_element(By.XPATH, Locators.password_input).send_keys(password)
        driver.find_element(By.XPATH, Locators.signin_button).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

#после успешной регистрации попадаем на страницу логина

    def test_incorrect_password(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, Locators.password_input).send_keys("1234")
        driver.find_element(By.XPATH, Locators.signin_button).click()
        incorrect_password = driver.find_element(By.CSS_SELECTOR, "p.input__error.text_type_main-default")
        assert "Некорректный пароль" == incorrect_password.text

    def test_name_field_not_empty(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, Locators.name_input).send_keys(TestData.user_name)
        name_field = driver.find_element(By.XPATH, Locators.name_value)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.text_to_be_present_in_element_value((By.XPATH, Locators.name_value), TestData.user_name))
        assert TestData.user_name == name_field.get_attribute("value")

    def test_password_length(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, Locators.password_input).send_keys(password)
        assert len(password) >= 6