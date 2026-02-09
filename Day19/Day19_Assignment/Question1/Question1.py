
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Edge()
driver.maximize_window()

# 1️⃣ Implicit Wait
driver.implicitly_wait(10)

driver.get("https://tutorialsninja.com/demo/")

print("Page opened with Implicit Wait applied.")

# 2️⃣ Explicit Wait - wait until the SEARCH box becomes clickable

wait = WebDriverWait(driver, 15)

search_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "search"))
)

print("Explicit Wait: Search box is clickable!")
search_box.send_keys("Laptop")

# 3️⃣ Fluent Wait - wait until the SEARCH button is visible
fluent_wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

search_button = fluent_wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-default.btn-lg"))
)

print("Fluent Wait: Search button is visible now!")
search_button.click()

# Close browser
time.sleep(5)
driver.quit()
