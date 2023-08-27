*** Settings ***
Documentation  Robot Framework Page Tests for www.tudorgall.com
Library  SeleniumLibrary
Library  Collections
Resource  Resources/variables.robot
Resource  Resources/keywords.robot

*** Test Cases ***
Navigate To Home Page
    [Tags]  home
    Open Site
    Navigate To Page  Home
    Check Page Title  ${HOME TITLE}

Click on the About Me Upper Button
    [Tags]  about
    Page Contains Upper and Lower Buttons
    Click Element  ${ABOUT ME UPPER BUTTON}
    Check Page Title    ${ABOUT ME TITLE}


Click on the CV Upper Button
    [Tags]    CV
    Page Contains Upper and Lower Buttons
    Click Element  ${CV UPPER BUTTON}
    Check Page Title    ${CV TITLE}

Click on the Contact Upper Button
    [Tags]    Contact
    Page Contains Upper and Lower Buttons
    Click Element    ${CONTACT UPPER BUTTON}
    Check Page Title    ${CONTACT TITLE}

Click on the Home Upper Button
    [Tags]    Home
    Page Contains Upper and Lower Buttons
    Click Element    ${HOME UPPER BUTTON}
    Check Page Title    ${HOME TITLE}
    Close Browser


