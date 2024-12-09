import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR,"button[role='none']").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(12)").click()
    time.sleep(5)
    request.cls.driver = driver
    yield
    driver.quit()
# CONFTEST

#
# import time
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser", action="store", default="firefox"
#     )
#
#
# @pytest.fixture(scope="class")
# def setup(request):
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "firefox":
#         driver = webdriver.Firefox()
#         driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#         time.sleep(5)
#         driver.find_element(By.CSS_SELECTOR, "li:nth-child(12)").click()
#         time.sleep(5)
#         request.cls.driver = driver
#     elif browser_name == "chrome":
#         driver = webdriver.Chrome()
#         driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#         time.sleep(5)
#         driver.find_element(By.CSS_SELECTOR, "li:nth-child(12)").click()
#         time.sleep(5)
#         request.cls.driver = driver
#     elif browser_name == "Egde":
#         driver = webdriver.Edge()
#         driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#         time.sleep(5)
#         driver.find_element(By.CSS_SELECTOR, "li:nth-child(12)").click()
#         time.sleep(5)
#         request.cls.driver = driver
