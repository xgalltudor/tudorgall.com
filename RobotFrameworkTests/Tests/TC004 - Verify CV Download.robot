*** Settings ***
Documentation  Robot Framework Page Tests for www.tudorgall.com
Library  SeleniumLibrary
Library  Collections
Library  OperatingSystem
Resource  Resources/variables.robot
Resource  Resources/keywords.robot
Test Setup    Open Site
Test Teardown    Close All Browsers

*** Test Cases ***
Navigate to CV Page and check the PDF CV Downloads
    User Is On Home Page
    Click Element   ${CV UPPER BUTTON}
    User Is On CV Page
    Verify PDF Opens in New Tab when the User clicks on "Download my PDF Curriculum Vitae"


    
