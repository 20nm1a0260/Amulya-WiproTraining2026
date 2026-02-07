
#! Synchronization --- implict wait and explict wait 

#* conditional synchronization and Unconditional synchronization


# unconditional synchronization - time.sleep()

#conditional synchronization- Implict wait and Explict wait

#& Implict Wait

'''
 Implict wait
. Implicit Wait
. By configuring implicit wait, here we are telling the WebDriver to poll the DOM
for a specified amount of time when trying to find an elelnent
. The default setting is 0 seconds
. Once set, the timeout is set for the life of the driver, until it is changed again
. It is a mechanism which will be written once and applied for entire session
automatically
. If we set implicit wait, find element will not throw an exception if the element is
not found in first instance, instead it will poll for the element until the timeout
and then proceeds further
. Example:
driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
'''

#& Explict wait

'''
Explict wait:
Explicit Wait
. Explicit Wait tells the WebDriver to Wait until the specified condition is met or
maximum time elapses before throwing NoSuchElement (or) ElementNotVisible
Exceptions
. WebDriverWait in combination with ExpectedCondition is one way this can be
accomplished
. Explicit waits are applied for the specified test step In test script
. Expected Conditions
. These are a set of common conditions that can be used with the WebDriverWait
class to check on the state of an object
Example:
WebDriverWait wait = new WebDriverWait(driver, 10);
WebElement element
wait.until(ExpectedConditions.elementToBeClickable(By.id("chk1")));

'''

#!  Javascript executer 

#*  refer Selenium_Jsexecuter.py file

#! Page object

#* Refer Selenium_Page_Object.py file and Loginpage.py
