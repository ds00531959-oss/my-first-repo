import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_cases(driver):

    test_cases = [
        ("furqan.shaikh@artivatic.ai","wrongpass"),
        ("wronguser@test.com","Furquan@dev1!"),
        ("wronguser@test.com","wrongpass"),
        ("furqan.shaikh@artivatic.ai","Furquan@dev1!")
    ]

    for email,password in test_cases:

        driver.get("https://health-claim-ui-prod.artivatic.ai/auth/login")
        time.sleep(5)

        driver.find_element(By.ID,"empId").send_keys(email)

        driver.find_element(By.ID,"password").send_keys(password)

        Select(driver.find_element(By.ID,"cn")).select_by_visible_text("India")

        driver.find_element(By.XPATH,"//button[contains(text(),'LOGIN')]").click()

        time.sleep(3)

        print("Test executed for:", email, password)

        # simple assertion
        assert driver.current_url is not None