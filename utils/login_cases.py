from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://health-claim-ui-prod.artivatic.ai/auth/login")

time.sleep(5)

# test cases
test_cases = [
    ("furqan.shaikh@artivatic.ai","wrongpass"),   # Case 1 → user correct, password wrong
    ("wronguser@test.com","Furquan@dev1!"),       # Case 2 → user wrong, password correct
    ("wronguser@test.com","wrongpass"),           # Case 3 → both wrong
    ("furqan.shaikh@artivatic.ai","Furquan@dev1!")# Case 4 → both correct
]

for email,password in test_cases:

    # refresh page for next test
    driver.get("https://health-claim-ui-prod.artivatic.ai/auth/login")
    time.sleep(5)

    # email
    driver.find_element(By.ID,"empId").send_keys(email)

    # password
    driver.find_element(By.ID,"password").send_keys(password)

    # country select
    Select(driver.find_element(By.ID,"cn")).select_by_visible_text("India")

    # login click
    driver.find_element(By.XPATH,"//button[contains(text(),'LOGIN')]").click()

    time.sleep(3)

    print("Test executed for:",email,password)

input("Press Enter to close browser...")

driver.quit()