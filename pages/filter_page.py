from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_filter(self):
        btn = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//p[text()='Advanced Filter']")
        ))
        self.driver.execute_script("arguments[0].click();", btn)

    def clear_filter(self):
        try:
            clear_btn = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Clear')]")
            ))
            self.driver.execute_script("arguments[0].click();", clear_btn)
        except:
            pass

    def select_claim_type(self, name):
        label = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//label[contains(text(),'{name}')]")
        ))

        checkbox_id = label.get_attribute("for")
        checkbox = self.driver.find_element(By.ID, checkbox_id)

        self.driver.execute_script("arguments[0].click();", checkbox)

    def apply_filter(self):
        btn = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Apply Filters')]")
        ))
        self.driver.execute_script("arguments[0].click();", btn)

    def get_count(self):
        elements = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//span[contains(@class,'item')]")
        ))

        for el in elements:
            txt = el.text.strip()
            if txt.isdigit():
                return int(txt)

        return 0