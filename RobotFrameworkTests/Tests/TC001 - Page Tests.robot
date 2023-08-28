*** Settings ***
Documentation  Robot Framework Page Tests for www.tudorgall.com
Library  SeleniumLibrary
Library  Collections
Resource  RobotFrameworkTests/Resources/keywords.robot
Suite Setup    Open Site
Suite Teardown    Close All Browsers

*** Test Cases ***
Navigate Directly To Home Page
    [Tags]  Home
    Navigate To Page  Home
    User Is On Home Page

Navigate Directly To About Me Page
    [Tags]    About
    Navigate To Page  About me
    User Is On About Me Page

Navigate Directly To Curriculum Vitae Page
    [Tags]  CV
    Navigate To Page  CV
    User Is On CV Page

Navigate Directly To Contact Page
    [Tags]  Contact
    Navigate To Page  Contact
    User Is On Contact Page
