
#& Data driven Test Cases

#---> using data for validation of login details or something is called data driven test cases.
#---> refer "Robotframework" folder ->> "test4_datadriven.robot" file


#! getting arguments from the excel sheet

#& steps 
#* Install this : pip install robotframework-datadriver
#*  pip install pandas openpyxl

#---> refer "Robotframework" and in that  go to test5_excel.robot file and excel file is test5data.xlsx 

#&  UNDERSTANDING SUITE SETUP  &#

'''✅ What is Suite Setup?

Suite Setup runs ONCE before all test cases in that file start.

Think of it like:

👉 "Prepare everything before tests begin"

Example
*** Settings ***
Suite Setup    Open Browser

*** Keywords ***
Open Browser
    Open Browser    https://google.com    chrome

If you have 5 test cases:

Browser opens only once

Then all tests run

Browser stays open

✅ What is Suite Teardown?

Suite Teardown runs ONCE after all test cases finish.

Think of it like:

👉 "Clean everything after tests finish"

Example
*** Settings ***
Suite Teardown    Close Browser


After all tests finish:

Browser closes once

🧠 Easy Real-Life Example

Imagine writing an exam:

Concept	Real Life Example
Suite Setup	Enter exam hall
Test Case	Write each subject
Suite Teardown	Leave exam hall

You enter once.
You leave once.
'''

#! tutorial ninja automation with excel 

# refer --> test6_tutorialninja.robot and test6data.xlsx

#! tutorial ninja automation using csv file 

#refer --> test7_tutorialninja.robot and test7data.csv
