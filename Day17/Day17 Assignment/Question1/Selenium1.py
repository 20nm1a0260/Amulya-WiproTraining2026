
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Edge()
driver.maximize_window()

# Wait object
wait = WebDriverWait(driver, 15)

# Open website
driver.get("https://demoqa.com/automation-practice-form")

# Fill text boxes
wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Sai")
driver.find_element(By.ID, "lastName").send_keys("Prakash")
driver.find_element(By.ID, "userEmail").send_keys("sai@test.com")
driver.find_element(By.ID, "userNumber").send_keys("9988776655")

# Select radio button (handle ads safely)

male_radio = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//label[text()='Male']"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", male_radio)
driver.execute_script("arguments[0].click();", male_radio)

# Select checkbox
sports_checkbox = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//label[text()='Sports']"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sports_checkbox)
driver.execute_script("arguments[0].click();", sports_checkbox)

# Select State dropdown
state_dropdown = wait.until(
    EC.element_to_be_clickable((By.ID, "state"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state_dropdown)
state_dropdown.click()

ncr_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']"))
)
ncr_option.click()

# Submit form
submit_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
driver.execute_script("arguments[0].click();", submit_btn)

# Verify confirmation
confirmation = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "modal-title"))
).text

if "Thanks for submitting the form" in confirmation:
    print("✅ Form submitted successfully")
else:
    print("❌ Form submission failed")

driver.quit()
