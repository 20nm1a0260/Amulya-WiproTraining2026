*** Keywords ***
Register New User
    [Arguments]    ${firstname}    ${lastname}    ${password}    ${gender}

    Click Link    Register
    Wait Until Page Contains    Register    10s

    Run Keyword If    '${gender}' == 'Male'    Click Element    id=gender-male
    ...    ELSE    Click Element    id=gender-female

    ${random}=    Evaluate    __import__('uuid').uuid4().hex[:6]
    ${email}=     Set Variable    user_${random}@test.com

    Input Text    id=FirstName    ${firstname}
    Input Text    id=LastName     ${lastname}
    Input Text    id=Email        ${email}
    Input Text    id=Password     ${password}
    Input Text    id=ConfirmPassword    ${password}

    Click Button    id=register-button

    Wait Until Page Contains    Your registration completed    15s

    Click Button    xpath=//input[@value='Continue']

    [Return]    ${email}