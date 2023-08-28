*** Settings ***
Documentation  Robot Framework Page Tests for www.tudorgall.com
Library  SeleniumLibrary
Library  Collections
Resource  ../Resources/variables.robot
Resource  ../Resources/keywords.robot
Test Setup    Open Site
Test Teardown    Close All Browsers

*** Test Cases ***
Navigate To Home Page and interact with inner elements
    [Tags]  Home
    User Is On Home Page
    Click Element   ${LETS TALK BUTTON}
    User Is On Contact Page
    Click Element   ${TG MAIN BUTTON}
    User Is On Home Page
    Click Element   ${CONTACT ME BUTTON}
    User Is On Contact Page
    Click Element   ${TG SECONDARY BUTTON}
    User Is On Home Page
    Click Element   ${MAIN SKILLS}
    User Is On CV Page
    Click Element   ${CONTACT ME BUTTON}
    User Is On Contact Page
    Click Element   ${HOME UPPER BUTTON}
    User Is On Home Page

Navigate to Contact Page and check Social Media buttons
    [Tags]  Contact  SocialMedia
    User Is On Home Page
    Click Element    ${CONTACT ME BUTTON}
    User Is On Contact Page
    Verify Social Media Link Opens In New Tab  ${LINKEDIN}  ${LINKEDIN URL}
    Verify Social Media Link Opens In New Tab  ${WHATSAPP}  ${WHATSAPP URL}
    Verify Social Media Link Opens In New Tab  ${GITHUB}  ${GITHUB URL}
    Verify Social Media Link Opens In New Tab  ${FACEBOOK}  ${FACEBOOK URL}
    Verify Social Media Link Opens In New Tab  ${INSTAGRAM}  ${INSTAGRAM URL}
    Verify Social Media Link Opens In New Tab  ${TWITTER}  ${TWITTER URL}

Navigate ro Contact Page and check Email and Phone Links
    [Tags]  Contact  Email  Phone
    User Is On Home Page
    Click Element    ${CONTACT LOWER BUTTON}
    User Is On Contact Page
    Verify email or phone link  ${YAHOO MAIL}  ${YAHOO MAIL LINK}
    Verify email or phone link  ${GOOGLE MAIL}  ${GOOGLE MAIL LINK}
    Verify email or phone link  ${PHONE NUMBER}  ${PHONE NUMBER LINK}