
*** Settings ***
Library    SeleniumLibrary

Suite Setup    Open Browser    http://127.0.0.1:5000/form    chrome
Suite Teardown    Close Browser

*** Test Cases ***
Register Patient
    Input Text    name=patient_name    Sai
    Input Text    name=age    30
    Click Element    xpath=//input[@value='male']
    Input Text    name=contact    9876543210
    Input Text    name=disease    fever
    Select From List By Label    name=doctor_assigned    Dr. Sharat
    Click Button    xpath=//input[@type='submit']
    Wait Until Page Contains    Details Submitted Successfully
