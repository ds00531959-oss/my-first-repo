from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome()

driver.get("https://health-claim-ui-prod.artivatic.ai/auth/login")

wait = WebDriverWait(driver,20)

# email
email = wait.until(EC.element_to_be_clickable((By.ID,"empId")))
email.send_keys("furqan.shaikh@artivatic.ai")

# password
driver.find_element(By.ID,"password").send_keys("Furquan@dev1!")

# country
Select(driver.find_element(By.ID,"cn")).select_by_visible_text("India")

# login
driver.find_element(By.XPATH,"//button[contains(text(),'LOGIN')]").click()

# wait dashboard
wait.until(EC.url_contains("dashboard"))
time.sleep(5)

print("Login Successful")

# -----------------------------
# Dashboard Metrics
# -----------------------------

metrics = driver.find_elements(By.XPATH,"//div[contains(@class,'card')]//h3")
labels  = driver.find_elements(By.XPATH,"//div[contains(@class,'card')]//p")

data = {}

for label,value in zip(labels,metrics):
    data[label.text] = value.text

print("Dashboard Data:",data)

# -----------------------------
# Excel Report
# -----------------------------

df = pd.DataFrame([data])
df.to_excel("claim_dashboard_report.xlsx", index=False)

print("Excel Report Generated")

input("Press Enter to close browser...")

driver.quit()