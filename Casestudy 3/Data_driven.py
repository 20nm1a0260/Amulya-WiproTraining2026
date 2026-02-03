
***Settings***
Library        SeleniumLibrary

*** Test Cases ***
Register Multiple Patients
    [Template]    Register Patient

    Ravi    40    male    9998887776    fever    Dr. Seenu
    Meena   28    female  8887776665    cold     Dr. Neha

*** Keywords ***
Register Patient
    [Arguments]    ${name}    ${age}    ${gender}    ${contact}    ${disease}    ${doctor}
    Open Browser        http://127.0.0.1:5000/form    chrome
    Input Text    name=patient_name    ${name}
    Input Text    name=age    ${age}
    Click Element    xpath=//input[@value='${gender}']
    Input Text    name=contact    ${contact}
    Input Text    name=disease    ${disease}
    Select From List By Label    name=doctor_assigned    ${doctor}
    Click Button    xpath=//input[@type='submit']
    Sleep    2
    Close Browser
