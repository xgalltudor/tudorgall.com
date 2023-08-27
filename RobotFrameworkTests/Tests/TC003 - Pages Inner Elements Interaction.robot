*** Settings ***
Documentation  Robot Framework Page Tests for www.tudorgall.com
Library  SeleniumLibrary
Library  Collections
Resource  Resources/variables.robot
Resource  Resources/keywords.robot

*** Test Cases ***
Navigate To Home Page and interact with inner elements
    [Tags]  Home
    Open Site
    User Is On Home Page
    Click Element  ${LETS TALK BUTTON}
    User Is On Contact Page
    Click Element  ${TG MAIN BUTTON}
    User Is On Home Page
    Click Element    ${CONTACT ME BUTTON}
    User Is On Contact Page
    Click Element    ${TG SECONDARY BUTTON}
    User Is On Home Page



