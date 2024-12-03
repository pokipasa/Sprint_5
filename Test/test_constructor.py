import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

login = f'testtestov{random.randint(1000, 99999)}@yandex.ru'
password = [
    random.choice(string.ascii_lowercase + string.digits if i != 5 else string.ascii_uppercase) for i in range(10)
]


class TestConstructorSection:
    def test_click_to_section_sauce(self, driver, login_fixture):

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_sauce).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.selected_sauce)))
        current_tab = driver.find_element(By.XPATH,Locators.selected_sauce)
        assert current_tab.is_displayed()

    def test_click_to_section_topping(self, driver, login_fixture):
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_topping).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.selected_topping)))
        current_tab = driver.find_element(By.XPATH,Locators.selected_topping)
        assert current_tab.is_displayed()

    def test_click_to_section_bread(self, driver, login_fixture):
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_topping).click()
        driver.find_element(By.XPATH, Locators.constructor_bread).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.selected_bread)))
        current_tab = driver.find_element(By.XPATH,Locators.selected_bread)
        assert current_tab.is_displayed()