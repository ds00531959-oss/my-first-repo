from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ---------- CONFIG ----------
BASE_URL = "YOUR_BASE_URL"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

# ---------- DRIVER SETUP ----------
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

try:
    # ---------- LOGIN ----------
    driver.get(f"{BASE_URL}/auth/login")

    username = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    password.send_keys(Keys.RETURN)

    # ---------- WAIT FOR DASHBOARD ----------
    wait.until(EC.url_contains("dashboard"))

    # ---------- WAIT FOR LOADER TO DISAPPEAR (if exists) ----------
    try:
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loader")))
    except:
        pass  # ignore if loader not present

    # ---------- CLICK ADVANCE FILTER ----------
    advance_filter = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Advance Filter')]"))
    )

    # Scroll to element (safe practice)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", advance_filter)

    # Try normal click first
    try:
        advance_filter.click()
    except:
        # fallback if click intercepted
        driver.execute_script("arguments[0].click();", advance_filter)

    print("Advance Filter clicked successfully")

    # ---------- OPTIONAL: VERIFY FILTER PANEL OPEN ----------
    # Example (update locator as per UI)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'filter-panel')]")))
    print("Advance Filter panel opened successfully")

except Exception as e:
    print("Error occurred:", str(e))

finally:
    driver.quit()