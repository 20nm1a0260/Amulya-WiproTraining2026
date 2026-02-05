
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
import time

driver=webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
wait=WebDriverWait(driver,10)

#~  this is normal alert message display

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button').click()
alert=driver.switch_to.alert
print(alert.text)
time.sleep(5)

#~ accepting the alert box 

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button').click()
alert=driver.switch_to.alert
time.sleep(3)
alert.accept()
print("you clicked ok")

#~ prompting into the alert box and verifying that message displayed on the page

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()
alert=driver.switch_to.alert
time.sleep(5)
alert.send_keys("Saiprakash")
alert.accept()
message=driver.find_element(By.XPATH,'//p[@id="result"]').text
print(message)
