
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Labpage:
    
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)

    desktops_link = (By.LINK_TEXT, "Desktops")
    mac_link = (By.LINK_TEXT, "Mac (1)")
    mac_heading=(By.XPATH,'//*[@id="content"]/h2')
    sort_dropdown = (By.ID, "input-sort")
    add_to_cart=(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]/span')
    search=(By.NAME,"search")
    searchbutton=(By.XPATH,"//*[@id='search']/span/button")
    clickbox=(By.NAME,"description")
    clickboxbutton=(By.ID,"button-search")

    def desktops(self):
        self.driver.find_element(*self.desktops_link).click()

    def mac(self):
        self.driver.find_element(*self.mac_link).click()

    def verify_mac_heading(self):
        heading = self.wait.until(
        EC.visibility_of_element_located(self.mac_heading)
    )
        assert heading.text == "Mac"
        print("Mac heading verified successfully")

    def select_sort_option(self, visible_text):
        dropdown_element = self.wait.until(
            EC.presence_of_element_located(self.sort_dropdown)
        )
        select = Select(dropdown_element)
        select.select_by_visible_text(visible_text)
    
    def cart(self):
        self.driver.find_element(*self.add_to_cart).click()
    
    def searchinput(self,searchtext):
        searchbox=self.wait.until(
            EC.presence_of_element_located(self.search)
        )
        searchbox.clear()
        self.driver.find_element(*self.search).send_keys(searchtext)
    
    def searchclick(self):
        button = self.wait.until(
        EC.element_to_be_clickable(self.searchbutton)
    )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()

    def clickboxclick(self):
        self.driver.find_element(*self.clickbox).click()

    def clicksearch(self):
        self.driver.find_element(*self.clickboxbutton).click()
