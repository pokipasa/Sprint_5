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


class TestLogout:
    def test_logout(self, driver, login_fixture):

        driver.find_element(By.XPATH, Locators.personal_account_button).click()
        logout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.logout_button)))
        logout.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"