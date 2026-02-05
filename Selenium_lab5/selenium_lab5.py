
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time

#! Part 1: Launch Application

driver=webdriver.Edge()
driver.maximize_window()
wait=WebDriverWait(driver,15)

driver.get("https://tutorialsninja.com/demo/")

#~ check the title 

actual_title=driver.title

if actual_title=="Your Store":
    print("Title Verified")
else:
    print("Title Not Verified")

#~ click myaccount

my_account=wait.until(
    EC.element_to_be_clickable((By.XPATH,"//span[text()='My Account']"))
)
my_account.click()

#~ click register option

register_option=wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT,"Register"))
)
register_option.click()

register_heading=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h1[text()='Register Account']" ))
).text

if register_heading=="Register Account":
    print("Register heading verified")
else:
    print("Register heading not verified")

# driver.find_element(By.ID,"input-firstname").send_keys("saiprakash")
# driver.find_element(By.ID,"input-lastname").send_keys("reddy")
# driver.find_element(By.ID,"input-email").send_keys("sai12345@gmail.com")
# driver.find_element(By.ID,"input-telephone").send_keys(9876543210)

# password_scroll=driver.find_element(By.ID,"input-password")
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", password_scroll)

# driver.find_element(By.ID,"input-password").send_keys("12345")
# driver.find_element(By.ID,"input-confirm").send_keys("12345")
# driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
# driver.find_element(By.XPATH,"//input[@type='submit']").click()

# warning_msg=wait.until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
# ).text

# if warning_msg=="Warning: You must agree to the Privacy Policy!":
#     print("warning message verified")
# else:
#     print("warning message not verified")


#! Part 2: For 'Your Personal Details

# #~ first name validation

# longtext="sai"*15
# first_name = driver.find_element(By.ID, "input-firstname")
# first_name.clear()
# first_name.send_keys(longtext)
# driver.find_element(By.XPATH, "//input[@value='Continue']").click()
# try:
#     first_error = wait.until(
#         EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'First Name')]"))
#     ).text
#     print("First Name Error:", first_error)
# except:
#     print("No First Name Error")

# #~ lastname validation

# last_name = driver.find_element(By.ID, "input-lastname")
# last_name.clear()
# last_name.send_keys(longtext)

# driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# try:
#     last_error = wait.until(
#         EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Last Name')]"))
#     ).text
#     print("Last Name Error:", last_error)
# except:
#     print("No Last Name Error")

# driver.find_element(By.ID,"input-email").send_keys("sai111234335@gmail.com")

# #~ telephone number validation

# telephone=driver.find_element(By.ID,"input-telephone")
# telephone.clear()
# telephone.send_keys("12")

# driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# try:
#     tel_error = wait.until(
#         EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Telephone')]"))
#     ).text
#     print("Telephone Error:", tel_error)
# except:
#     print("Telephone accepted")


# password_scroll=driver.find_element(By.ID,"input-password")
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", password_scroll)

# driver.find_element(By.ID,"input-password").send_keys("12345")
# driver.find_element(By.ID,"input-confirm").send_keys("12345")
# driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
# driver.find_element(By.XPATH,'//input[@name="agree"]').click()
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# time.sleep(10)

#! part 3 password validation

# driver.find_element(By.ID,"input-firstname").send_keys("saiprakash")
# driver.find_element(By.ID,"input-lastname").send_keys("reddy")
# driver.find_element(By.ID,"input-email").send_keys("sai12345@gmail.com")
# driver.find_element(By.ID,"input-telephone").send_keys(9876543210)

# password_scroll=driver.find_element(By.ID,"input-password")

# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", password_scroll)

# #~ password validation

# password =driver.find_element(By.ID,"input-password")
# confirm=driver.find_element(By.ID,"input-confirm")
# password.clear()
# confirm.clear()
# password.send_keys("123")
# confirm.send_keys("123")

# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# try:
#     pass_fail=wait.until(
#         EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Password')]"))
#     ).text
#     print("Password Error",pass_fail)
# except:
#     print("Password Accepted")

# driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# time.sleep(5)

#! Part 4: For 'Newsletter'

# driver.find_element(By.ID,"input-firstname").send_keys("saiprakash")
# driver.find_element(By.ID,"input-lastname").send_keys("reddy")
# driver.find_element(By.ID,"input-email").send_keys("sai12332224225@gmail.com")
# driver.find_element(By.ID,"input-telephone").send_keys(9876543210)

# password_scroll=driver.find_element(By.ID,"input-password")
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", password_scroll)

# driver.find_element(By.ID,"input-password").send_keys("12345")
# driver.find_element(By.ID,"input-confirm").send_keys("12345")
# driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
# driver.find_element(By.XPATH,'//input[@name="agree"]').click()
# driver.find_element(By.XPATH,"//input[@type='submit']").click()

# wait=WebDriverWait(driver,10)

# expected_verify_message=wait.until(
#     EC.visibility_of_element_located((By.XPATH,'//*[@id="content"]/h1')
# )).text

# if expected_verify_message=="Your Account Has Been Created!":
#     print("Message Verified")
# else:
#     print("Message Not Verified")

# driver.find_element(By.XPATH,"//a[text()='Continue']").click()

# driver.find_element(By.LINK_TEXT,"View your order history")
