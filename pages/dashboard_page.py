from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    cards = (By.XPATH, "//div[contains(@class,'upper_card')]")

    def get_dashboard_counts(self):
        cards = self.wait.until(EC.presence_of_all_elements_located(self.cards))

        results = {}

        for card in cards:
            try:
                full_text = card.text.strip()

                if "Advanced Filter" in full_text:
                    continue

                lines = [line.strip() for line in full_text.split("\n") if line.strip()]

                label = None
                value = None

                for line in lines:
                    numbers = re.findall(r"\d+", line)

                    if numbers:
                        value = "".join(numbers)
                    else:
                        label = line

                if label and value:
                    results[label] = value

            except:
                continue

        return results