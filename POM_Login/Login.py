# Page object model
# reduce code or reusing code
# here all locators will be in one place for that one particular model
import time

from selenium.webdriver.common.by import By
from utility.Baseclass import Basepage


class Login(Basepage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit = (By.CSS_SELECTOR, '.oxd-button')
    click = (By.CSS_SELECTOR, '.oxd-userdropdown-name')
    Logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, namevalue, pwdvalue):
        self.hrm_send_keys(self.username, namevalue)
        self.hrm_send_keys(self.password, pwdvalue)
        self.hrm_btn_click(self.submit)
        time.sleep(8)

    def logout(self):
        self.hrm_btn_click(self.click)
        self.hrm_btn_click(self.Logout)
        time.sleep(3)

    def get_title(self, title):
        self.hrm_get_title(title)

# LOGIN
