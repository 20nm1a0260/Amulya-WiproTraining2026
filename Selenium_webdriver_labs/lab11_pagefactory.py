
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Labpagefactory:
    
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def desktops_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Desktops")
    
    @property
    def mac_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Mac (1)")
    
    @property
    def mac_heading(self):
        return self.driver.find_element(By.XPATH,'//*[@id="content"]/h2')
    
    @property
    def sort_dropdown(self):
        return self.driver.find_element(By.ID, "input-sort")
    
    @property
    def add_to_cart(self):
        return self.driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]/span')
    
    @property
    def search(self):
        return self.driver.find_element(By.NAME,"search")
    
    @property
    def searchbutton(self):
        return self.driver.find_element(By.XPATH,"//*[@id='search']/span/button")
    
    @property
    def clickbox(self):
        return self.driver.find_element(By.NAME,"description")
    
    @property
    def clickboxbutton(self):
        return self.driver.find_element(By.ID,"button-search")

    def desktops(self):
        self.desktops_link.click()

    def mac(self):
        self.mac_link.click()

    def verify_mac_heading(self):
        heading = self.wait.until(
        EC.visibility_of(self.mac_heading)
    )
        assert heading.text == "Mac"
        print("Mac heading verified successfully")

    def select_sort_option(self, visible_text):
        dropdown_element = self.wait.until(
            EC.visibility_of(self.sort_dropdown)
        )
        select = Select(dropdown_element)
        select.select_by_visible_text(visible_text)
    
    def cart(self):
        self.add_to_cart.click()
    
    def searchinput(self,searchtext):
        searchbox=self.wait.until(
            EC.visibility_of(self.search)
        )
        searchbox.clear()
        self.search.send_keys(searchtext)
    
    def searchclick(self):
        button = self.wait.until(
        EC.element_to_be_clickable(self.searchbutton)
    )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()

    def clickboxclick(self):
        self.clickbox.click()

    def clicksearch(self):
        self.clickboxbutton.click()
