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

Home Page Contains Inner Elements
    Wait Until Page Contains Element  ${LETS TALK BUTTON}
    Wait Until Page Contains Element  ${CONTACT ME BUTTON}
    Wait Until Page Contains Element  ${MAIN SKILLS}

About Me Page Contains Inner Elements
    Wait Until Page Contains Element  ${CONTACT ME BUTTON}

CV Page Contains Inner Elements
    Wait Until Page Contains Element  ${CONTACT ME BUTTON}
    Wait Until Page Contains Element  ${ANRITSU}
    Wait Until Page Contains Element  ${CONTINENTAL}
    Wait Until Page Contains Element  ${NESS}
    Wait Until Page Contains Element  ${BARRA}
    Wait Until Page Contains Element  ${DIMA}
    Wait Until Page Contains Element  ${ETTI}
    Wait Until Page Contains Element  ${NEGRUZZI}
    Wait Until Page Contains Element  ${DOWNLOAD CV}

Contact Page Contains Inner Elements
    Wait Until Page Contains Element  ${LINKEDIN}
    Wait Until Page Contains Element  ${WHATSAPP}
    Wait Until Page Contains Element  ${GITHUB}
    Wait Until Page Contains Element  ${FACEBOOK}
    Wait Until Page Contains Element  ${INSTAGRAM}
    Wait Until Page Contains Element  ${TWITTER}
    Wait Until Page Contains Element  ${SUBMIT BUTTON}

User is on Home Page
    [Tags]  home
    Check Page Title  ${HOME TITLE}
    Page Contains Upper and Lower Buttons
    Home Page Contains Inner Elements

User is on About Me Page
    [Tags]    About
    Check Page Title  ${ABOUT ME TITLE}
    Page Contains Upper and Lower Buttons
    About Me Page Contains Inner Elements

User is on CV Page
    [Tags]  CV
    Check Page Title  ${CV TITLE}
    Page Contains Upper and Lower Buttons
    CV Page Contains Inner Elements

User is on Contact Page
    [Tags]  Contact
    Check Page Title  ${CONTACT TITLE}
    Page Contains Upper and Lower Buttons
    Contact Page Contains Inner Elements


