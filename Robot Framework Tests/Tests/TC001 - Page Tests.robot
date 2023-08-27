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

Navigate To About Me Page
    [Tags]    AboutMe
    Navigate To Page  About Me
    Check Page Title  ${ABOUT ME TITLE}

Navigate To Curriculum Vitae Page
    [Tags]  CV
    Navigate To Page  CV
    Check Page Title  ${CV TITLE}

Navigate To Contact Page
    [Tags]  Contact
    Navigate To Page  Contact
    Check Page Title  ${CONTACT TITLE}
    Close Browser
