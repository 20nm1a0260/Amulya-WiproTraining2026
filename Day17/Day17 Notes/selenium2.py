
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#find_elements

driver= webdriver.Edge()
driver.get("https://www.flipkart.com")
time.sleep(5)
links=driver.find_elements(By.TAG_NAME,"a")

for link in links:
    url=link.get_attribute("href")
    text=link.text.strip()
    print(text)
