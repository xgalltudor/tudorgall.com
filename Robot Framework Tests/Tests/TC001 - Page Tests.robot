*** Settings ***
Documentation  Robot Framework Page Tests for www.tudorgall.com
Library  SeleniumLibrary

*** Variables ***
    ${URL}  https://www.tudorgall.com
    ${BROWSER}  Chrome

*** Test Cases ***

Navigate To Home Page
    [Tags]  Home
    Open Browser  ${URL}  ${BROWSER}
    Title Should Be  Tudor Gall – Test Automation Developer
    Close Browser

Navigate To About Me Page
    [Tags]  AboutMe
    Open Browser  ${URL}/about-me  ${BROWSER}
    Title Should Be  About Me – Tudor Gall
    Close Browser

Navigate To Curriculum Vitae Page
    [Tags]  CV
    Open Browser  ${URL}/curriculum-vitae  ${BROWSER}
    Title Should Be  Curriculum Vitae – Tudor Gall
    Close Browser

Navigate To Contact Page
    [Tags]  Contact
    Open Browser  ${URL}/contact  ${BROWSER}
    Title Should Be  Contact – Tudor Gall
    Close Browser
