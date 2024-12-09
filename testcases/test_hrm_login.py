import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Testparam1:

    @pytest.mark.parametrize('username, password', [
        ("Admin", "admin123"),
        ("Admin", "kannan123"),
        ("sanju", "admin123"),
        ("sanju", "sanju123")
    ])
    def test_login(self, username, password):
        # Setup WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        # Enter Username and Password
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(5)

        try:
            # Check if login is successful by looking for user dropdown
            self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").click()
            time.sleep(3)
            self.driver.find_element(By.LINK_TEXT, "Logout").click()
            time.sleep(3)
            print(f"Login successful for user: {username}")
        except Exception as e:
            print(f"Login failed for user: {username} with error: {str(e)}")
        finally:
            # Close the driver
            self.driver.close()

