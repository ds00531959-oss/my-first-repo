from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    username_input = (By.ID, "empId")
    password_input = (By.ID, "password")
    country_dropdown = (By.ID, "cn")
    login_button = (By.XPATH, "//button[contains(text(),'LOGIN')]")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

        Select(self.wait.until(EC.presence_of_element_located(self.country_dropdown))).select_by_visible_text("India")

        # wait for button clickable
        element = self.wait.until(EC.element_to_be_clickable(self.login_button))

        # scroll into view (important for headless)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # small wait for UI stability
        time.sleep(2)

        # JS click (fix intercepted issue)
        self.driver.execute_script("arguments[0].click();", element)