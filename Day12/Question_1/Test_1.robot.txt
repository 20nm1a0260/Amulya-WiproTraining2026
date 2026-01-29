*** Settings ***

Library           SeleniumLibrary

*** Variables ***

${Name}            SaiPrakash

${Course}        Robot Framework

@{Numbers}            1     2     3     4


*** Test Cases ***
Log Basic Information
    Log         Starting first test case
    Log To Console         Hello ${Name}
    Log To Console        Learning ${Course}
    Log        First test case completed
    Log         Starting second test case
    Log To Console     Marks are @{Numbers}
    Log         Second test case completed