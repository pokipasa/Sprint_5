from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


class TestLogout:
    def test_logout(self, driver, login_fixture):

        driver.find_element(By.XPATH, Locators.personal_account_button).click()
        logout = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.logout_button))
        )
        logout.click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(
            "https://stellarburgers.nomoreparties.site/login"
        ))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
