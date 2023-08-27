*** Variables ***
#   URL & BROWSER
${URL}                      https://www.tudorgall.com
${BROWSER}                  Chrome
# URL SLUGS
${HOME}                     home
${ABOUT ME}                 about
${CONTACT}                  contact
${CV}                       curriculum-vitae
&{PAGE_URLS}                Home=               About me=about          CV=curriculum-vitae     Contact=contact

# TITLES
${HOME TITLE}               Tudor Gall – Test Automation Developer
${ABOUT ME TITLE}           About me – Tudor Gall
${CV TITLE}                 Curriculum Vitae – Tudor Gall
${CONTACT TITLE}            Contact – Tudor Gall

# UPPER & LOWER BUTTONS
${HOME UPPER BUTTON}        xpath=(//a[normalize-space()='Home'])[1]
${HOME LOWER BUTTON}        xpath=(//a[normalize-space()='Home'])[2]
${ABOUT ME UPPER BUTTON}    xpath=(//a[normalize-space()='About me'])[1]
${ABOUT ME LOWER BUTTON}    xpath=(//a[normalize-space()='About me'])[2]
${CV UPPER BUTTON}          xpath=(//a[normalize-space()='Curriculum Vitae'])[1]
${CV LOWER BUTTON}          xpath=(//a[normalize-space()='Curriculum Vitae'])[2]
${CONTACT UPPER BUTTON}     xpath=(//a[normalize-space()='Contact'])[1]
${CONTACT LOWER BUTTON}     xpath=(//a[normalize-space()='Contact'])[2]

# Tudor Gall Home Redirect Buttons
${TG MAIN BUTTON}           xpath=(//a[normalize-space()='Tudor Gall'])[1]
${TG SECONDARY BUTTON}      xpath=(//a[@class='site-name'])[1]



