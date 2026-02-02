
#! Question 5 – Command Line Execution, Setup & Teardown (Coding)

#Topics Covered: Command line, Setup & Teardown

''' 
Write a Robot Framework test suite that:

1. Uses Suite Setup and Suite Teardown

2. Uses Test Setup and Test Teardown

3. Executes from the command line using:

Tags

Output directory

4. Generates log.html and report.html

5. Includes at least one tagged test case
'''
#& Ans ---> refer "test1.robot" in this folder DAY14 Assignment

#* useful info about this

'''
What This Suite Contains

✔ Suite Setup
✔ Suite Teardown
✔ Test Setup
✔ Test Teardown
✔ Tagged test cases
✔ Console logs
✔ Assertions

🧠 Execution Flow

When you run:

Suite Setup runs once

Test Setup runs before each test

Test executes

Test Teardown runs after each test

After all tests → Suite Teardown runs

#^ this is execution commands
Execute From Command Line

Open terminal inside folder.

🔹 Run All Tests
robot sample_suite.robot

🔹 Run Only Smoke Tagged Tests
robot --include smoke sample_suite.robot

🔹 Run with Custom Output Directory
robot -d results sample_suite.robot


This will generate:

results/
    log.html
    report.html
    output.xml

🔹 Combine Tags + Output Directory
robot -d results --include smoke sample_suite.robot
'''


#! Question 6 – Browser Automation & Built-in Libraries (Coding)

#Topics Covered: SeleniumLibrary, Built-in library

'''Write a Robot Framework test case that:

1. Opens a browser using SeleniumLibrary

2. Interacts with:

Text box

Radio button

Check box

Drop-down

3. Uses Built-in keywords:

Run Keyword If

Should Be Equal

Sleep

4. Validates form submission

5. Closes the browser and generates execution reports
'''
#& Ans: Refer Question2 folder and test2.robot file.
