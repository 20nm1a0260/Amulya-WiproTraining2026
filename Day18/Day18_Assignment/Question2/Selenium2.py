
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.maximize_window()
wait=WebDriverWait(driver,10)

driver.get("https://letcode.in/frame")

iframe=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(iframe)

driver.find_element(By.NAME,"fname").send_keys("saiprakash")
driver.find_element(By.NAME,"lname").send_keys("reddy")

driver.switch_to.default_content()

print("Switched back to main page")

driver.get("https://letcode.in/window")

parent_window = driver.current_window_handle

# Click button to open new window
driver.find_element(By.ID, "home").click()

time.sleep(2)


# Switch between windows & print titles

all_windows = driver.window_handles

for window in all_windows:
    driver.switch_to.window(window)
    print("Window Title:", driver.title)
    time.sleep(1)

# Close child window & return to parent

for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        driver.close()

# Switch back to parent
driver.switch_to.window(parent_window)

print("Returned to Parent Window:", driver.title)

time.sleep(2)
driver.quit()
