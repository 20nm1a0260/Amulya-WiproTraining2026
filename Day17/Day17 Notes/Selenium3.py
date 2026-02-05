from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
import time

driver = webdriver.Edge()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Desktops").click()
driver.find_element(By.LINK_TEXT, "Mac (1)").click()

dropdown = Select(driver.find_element(By.ID, "input-sort"))

wait = WebDriverWait(driver, 10)

# Print all dropdown options

for option in dropdown.options:
    print(option.text)

#setting dropdown option using index value

dropdown.select_by_index(4)