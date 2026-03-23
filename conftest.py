import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://health-claim-ui-prod.artivatic.ai/auth/login")
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.login("furqan.shaikh@artivatic.ai", "Furquan@dev1!")
    return driver