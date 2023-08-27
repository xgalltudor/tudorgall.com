*** Settings ***
Library  SeleniumLibrary
Library  Collections
Resource  variables.robot

*** Keywords ***
Open Site
    Open Browser  ${URL}  ${BROWSER}

Navigate To Page
    [Arguments]  ${page}
    ${url_slug}=  Get From Dictionary  ${PAGE_URLS}  ${page}
    Go To  ${URL}/${url_slug}

Check Page Title
    [Arguments]  ${title}
    Title Should Be  ${title}

Page Contains Upper and Lower Buttons
    Wait Until Page Contains Element  ${HOME UPPER BUTTON}
    Wait Until Page Contains Element  ${ABOUT ME UPPER BUTTON}
    Wait Until Page Contains Element  ${CV UPPER BUTTON}
    Wait Until Page Contains Element  ${CONTACT UPPER BUTTON}
    Wait Until Page Contains Element  ${HOME LOWER BUTTON}
    Wait Until Page Contains Element  ${ABOUT ME LOWER BUTTON}
    Wait Until Page Contains Element  ${CV LOWER BUTTON}
    Wait Until Page Contains Element  ${CONTACT LOWER BUTTON}
    Wait Until Page Contains Element  ${TG MAIN BUTTON}
    Wait Until Page Contains Element  ${TG SECONDARY BUTTON}
