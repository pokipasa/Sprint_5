import pytest
from selenium import webdriver
from locators import Locators
from selenium.webdriver.common.by import By
from test_data import TestData


@pytest.fixture()
def driver():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def login_fixture(driver):

    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, Locators.login_to_account_button).click()  # клик по кнопке "Войти в аккаунт"
    driver.find_element(By.XPATH, Locators.email_input).send_keys(TestData.email)  # вводим email в поле email
    driver.find_element(By.XPATH, Locators.password_input).send_keys(TestData.password)  # вводим пароль в поле пароль
    driver.find_element(By.XPATH, Locators.enter_button).click()  # клик по кнопке "Войти"
