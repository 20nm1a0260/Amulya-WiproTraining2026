*** Keywords ***
Login To Application
    [Arguments]    ${email}    ${password}

    Click Link    Log in
    Wait Until Page Contains    Welcome, Please Sign In!    10s

    Clear Element Text    id=Email
    Clear Element Text    id=Password

    Input Text    id=Email       ${email}
    Input Text    id=Password    ${password}

    Click Button  xpath=//input[@value='Log in']

    Wait Until Page Contains    Log out    15s


Logout From Application
    Click Link    Log out
    Wait Until Page Contains    Log in    10s