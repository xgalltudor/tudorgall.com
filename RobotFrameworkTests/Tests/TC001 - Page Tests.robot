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
    Page Contains Upper and Lower Buttons

Navigate To About Me Page
    [Tags]    About
    Navigate To Page  About me
    Check Page Title  ${ABOUT ME TITLE}
    Page Contains Upper and Lower Buttons

Navigate To Curriculum Vitae Page
    [Tags]  CV
    Navigate To Page  CV
    Check Page Title  ${CV TITLE}
    Page Contains Upper and Lower Buttons

Navigate To Contact Page
    [Tags]  Contact
    Navigate To Page  Contact
    Check Page Title  ${CONTACT TITLE}
    Page Contains Upper and Lower Buttons
    Close Browser
