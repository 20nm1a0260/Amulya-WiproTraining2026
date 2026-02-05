from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
import time

driver= webdriver.Edge()
driver.get("https://letcode.in/alert")


#* simple alert 

driver.find_element(By.ID,"accept").click()
alert=driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.accept()
driver.close()

#* confirm alert 

driver.find_element(By.ID,"confirm").click()
alert =driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.dismiss()

#* prompt alert

driver.find_element(By.ID,"prompt").click()
wait = WebDriverWait(driver, 10)
alert=driver.switch_to.alert
print(alert.text)
alert.send_keys("Hello Sai Prakash")
alert.accept()