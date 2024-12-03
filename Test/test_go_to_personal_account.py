from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


class TestPersonalAccount:
    def test_goto_personal_account(self, driver, login_fixture):
        driver.find_element(By.XPATH, Locators.personal_account_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
