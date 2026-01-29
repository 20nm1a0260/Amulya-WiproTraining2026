
#! ROBOT FRAMEWORK
'''
1. Introduction to Robot Framework
Robot Framework is an open-source test automation framework mainly used for:
Acceptance testing
Regression testing
RPA (Robotic Process Automation)
Key Features
Keyword-driven testing
Easy-to-read, tabular syntax
Supports Selenium, API, Database, Appium, etc.
Platform and language independent (written in Python)
File Types

#! .robot → test cases
#! .resource → reusable keywords
#! .py → custom libraries

2. Environment Setup & Required Packages
Step 1: Install Python
Check installation:

#~ python --version

Step 2: Install Robot Framework

#~ pip install robotframework

Verify:

#~ robot --version

Step 3: Install Selenium Library

#~ pip install robotframework-seleniumlibrary

Step 4: Install WebDriver

Use ChromeDriver / EdgeDriver
(or use WebDriverManager manually if preferred)

3. Robot Framework – RIDE Tool
What is RIDE?
RIDE (Robot IDE) is a GUI tool to:
Write test cases
Manage keywords
Execute tests

Install RIDE

#~ pip install robotframework-ride

Launch RIDE:

#~ ride.py

Then 

#! python -m robotide

After the command new window will open which is RIDE

1) there go to - file- create a new project and name it is 2026.

2) under Test suites create a new .robot test case , give "test1.robot"

3) on the right side , a tab will open go to the text edit and put 

Example: Simple Login Test
*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
Open Google ---> #^ test case name 
    Open Browser    https://www.google.com    chrome
    Title Should Be    Google
    Close Browser

4) save changes , go to run tab and click on start.

5) Adding keywords

*** Keywords ***
Open Application
    Open Browser    https://example.com    chrome
    Maximize Browser Window

'''

#! refer "robot framework" folder  for the classwork of 29-jan-2026  ---> "test1.robot","test2_Keywords.robot","test3_login.robot"
