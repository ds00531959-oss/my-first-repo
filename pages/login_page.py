from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()