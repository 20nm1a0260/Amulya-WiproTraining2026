
from selenium import webdriver
from Lab11pageFactory import  Labpagefactory
import time

driver=webdriver.Edge()

driver.get("https://tutorialsninja.com/demo/")

driver.maximize_window()

driver.implicitly_wait(10)

page=Labpagefactory(driver)

page.desktops()
page.mac()
page.verify_mac_heading()
page.select_sort_option("Price (Low > High)")
page.cart()

page.searchinput("Mobile")
page.searchclick()
page.clickboxclick()
page.clicksearch()

page.searchinput("Monitors")
page.searchclick()

driver.quit()
