*** Settings ***
Documentation  Robot Framework Page Tests for www.tudorgall.com
Library  SeleniumLibrary
Library  Collections
Library  OperatingSystem
Resource  ../Resources/variables.robot
Resource  ../Resources/keywords.robot
Test Setup    Open Site
Test Teardown    Close All Browsers

*** Test Cases ***
Try to submit a message without completing the required fields
    [Tags]    Contact
    User Is On Home Page
    Click Element   ${LETS TALK BUTTON}
    User Is On Contact Page
    Click Element    ${SUBMIT BUTTON}
    Element Should Not Be Visible   ${MESSAGE SENT}

Try to submit a message gradually completing the required fields
    [Tags]    Contact
    User Is On Home Page
    Click Element   ${LETS TALK BUTTON}
    User Is On Contact Page
    Click Element    ${SUBMIT BUTTON}
    Element Should Not Be Visible   ${MESSAGE SENT}
    Input Text    ${CONTACT NAME}   ${NAME INPUT}
    Click Element    ${SUBMIT BUTTON}
    Element Should Not Be Visible   ${MESSAGE SENT}
    Input Text    ${CONTACT EMAIL}  ${EMAIL INPUT}
    Click Element    ${SUBMIT BUTTON}
    Element Should Not Be Visible   ${MESSAGE SENT}
    Input Text    ${CONTACT PHONE}  ${PHONE INPUT}
    Click Element    ${SUBMIT BUTTON}
    Element Should Not Be Visible   ${MESSAGE SENT}
    Input Text    ${CONTACT MESSAGE}    ${MESSAGE INPUT}
    Click Element    ${SUBMIT BUTTON}
    Element Text Should Be    ${MESSAGE SENT}  ${MESSAGE SENT TEXT}

Submit a message completing the required fields
    [Tags]    Contact
    User Is On Home Page
    Click Element   ${LETS TALK BUTTON}
    User Is On Contact Page
    Input Text    ${CONTACT NAME}   ${NAME INPUT}
    Input Text    ${CONTACT EMAIL}  ${EMAIL INPUT}
    Input Text    ${CONTACT MESSAGE}    ${MESSAGE INPUT}
    Click Element    ${SUBMIT BUTTON}
    Element Text Should Be    ${MESSAGE SENT}  ${MESSAGE SENT TEXT}





    
