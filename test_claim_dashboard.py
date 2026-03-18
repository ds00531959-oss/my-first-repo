import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_dashboard_dynamic_counts(driver):

    wait = WebDriverWait(driver, 30)

    driver.get("https://health-claim-ui-prod.artivatic.ai/auth/login")

    # LOGIN
    wait.until(EC.element_to_be_clickable((By.ID, "empId"))).send_keys("furqan.shaikh@artivatic.ai")
    driver.find_element(By.ID, "password").send_keys("Furquan@dev1!")
    Select(driver.find_element(By.ID, "cn")).select_by_visible_text("India")
    driver.find_element(By.XPATH, "//button[contains(.,'LOGIN')]").click()

    # WAIT FOR DASHBOARD
    wait.until(EC.url_contains("dashboard"))
    print("Login done")

    # WAIT for cards to load
    cards = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[contains(@class,'card')]")
    ))

    print("\nDashboard Metrics:\n")

    # LOOP through each card
    for card in cards:
        try:
            # Get label
            label = card.find_element(By.XPATH, ".//p").text.strip()

            # Get value (try multiple possible tags)
            try:
                value = card.find_element(By.XPATH, ".//h3").text.strip()
            except:
                value = card.find_element(By.XPATH, ".//p[last()]").text.strip()

            print(f"{label} : {value}")

        except Exception as e:
            continue  # skip if any card structure mismatch