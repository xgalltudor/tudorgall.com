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

