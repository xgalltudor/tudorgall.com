*** Settings ***
Documentation  Robot Framework Page Tests for www.tudorgall.com
Library  SeleniumLibrary
Library  Collections
Resource  ../Resources/variables.robot
Resource  ../Resources/keywords.robot
Suite Setup    Open Site
Suite Teardown    Close All Browsers

*** Test Cases ***
Navigate To Home Page
    [Tags]  Home
    User Is On Home Page

Click on the About Me Upper Button
    [Tags]  About
    Click Element  ${ABOUT ME UPPER BUTTON}
    User Is On About Me Page

Click on the CV Upper Button
    [Tags]    CV
    Click Element  ${CV UPPER BUTTON}
    User Is On CV Page

Click on the Contact Upper Button
    [Tags]    Contact
    Click Element    ${CONTACT UPPER BUTTON}
    User Is On Contact Page

Click on the Home Upper Button
    [Tags]    Home
    Click Element    ${HOME UPPER BUTTON}
    User Is On Home Page

Click on the About Me Lower Button
    [Tags]  About
    Click Element  ${ABOUT ME LOWER BUTTON}
    User Is On About Me Page

Click on the CV Lower Button
    [Tags]    CV
    Click Element  ${CV LOWER BUTTON}
    User Is On CV Page

Click on the Contact Lower Button
    [Tags]    Contact
    Click Element    ${CONTACT LOWER BUTTON}
    User Is On Contact Page

Click on the Home Lower Button
    [Tags]    Home
    Click Element    ${HOME LOWER BUTTON}
    User Is On Home Page


