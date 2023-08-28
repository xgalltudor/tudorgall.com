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

Switch To New Tab
    ${windows}=    Get Window Handles
    Log     ${windows}
    ${NEW_WINDOW}=    Set Variable If    '${windows}[1]'!='${EMPTY}'    ${windows}[1]    ${EMPTY}
    Run Keyword If    '${NEW_WINDOW}'!='${EMPTY}'    Switch Window    ${NEW_WINDOW}
    Should Not Be Empty    ${NEW_WINDOW}    New tab did not open within the given time

Verify PDF Opens in New Tab when the User clicks on "Download my PDF Curriculum Vitae"
    ${MAIN_WINDOW}=    Get Window Handles
    Log     ${MAIN_WINDOW}
    Click Element    ${DOWNLOAD CV}
    Wait Until Keyword Succeeds    30 seconds    5 seconds    Switch To New Tab
    Location Should Be    ${CV_PDF_URL}

Verify Social Media Link Opens In New Tab
    [Arguments]    ${element_locator}    ${expected_url}
    # Verify the 'href' attribute contains the expected URL
    ${actual_url}=    Get Element Attribute    ${element_locator}  href
    Should Be Equal    ${actual_url}    ${expected_url}
    Log  Verified the 'href' attribute contains the expected URL

    # Verify the link is set to open in a new tab/window
    ${target_value}=    Get Element Attribute    ${element_locator}  target
    Should Be Equal    ${target_value}    _blank
    Log  Verified the link is set to open in a new tab/window

    # Click the link, which should open in a new tab
    Click Element    ${element_locator}
    Log  Clicked the link, which should open in a new tab

    # Switch to the newly opened tab
    ${all_handles}=    Get Window Handles
    ${new_handle}=    Get From List    ${all_handles}    -1
    Switch Window    ${new_handle}
    Log  Switched to the newly opened tab

    # Close the new tab and switch back to the original tab
    Wait Until Page Contains Element    tag:body    timeout=5s
    Close Window
    Log  Closed the newly opened tab
    ${original_handle}=    Get From List    ${all_handles}    0
    Switch Window    ${original_handle}
    Log  Switched back to the window

Verify email or phone link
    [Arguments]    ${element_locator}    ${expected_url}
    # Verify the 'href' attribute contains the expected URL
    ${actual_url}=    Get Element Attribute    ${element_locator}  href
    Should Be Equal    ${actual_url}    ${expected_url}
    Log  Verified the 'href' attribute contains the expected URL


