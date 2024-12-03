from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


class TestConstructorSection:
    def test_click_to_section_sauce(self, driver, login_fixture):

        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_sauce).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.selected_sauce))
        )
        current_tab = driver.find_element(By.XPATH,Locators.selected_sauce)
        assert current_tab.is_displayed()

    def test_click_to_section_topping(self, driver, login_fixture):
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_topping).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.selected_topping))
        )
        current_tab = driver.find_element(By.XPATH,Locators.selected_topping)
        assert current_tab.is_displayed()

    def test_click_to_section_bread(self, driver, login_fixture):
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_topping).click()
        driver.find_element(By.XPATH, Locators.constructor_bread).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.selected_bread))
        )
        current_tab = driver.find_element(By.XPATH, Locators.selected_bread)
        assert current_tab.is_displayed()
