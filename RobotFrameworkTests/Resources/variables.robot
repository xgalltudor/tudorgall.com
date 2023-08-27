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

# Inner elements
${LETS TALK BUTTON}         xpath=(//a[contains(text(),'Let’s talk!')])[1]
${CONTACT ME BUTTON}        xpath=(//a[normalize-space()='Contact me'])[1]
${SUBMIT BUTTON}            xpath=(//button[normalize-space()='Submit'])[1]
${MAIN SKILLS}              xpath=(//a[normalize-space()='Main skills'])[1]

# Companies
${ANRITSU}                  xpath=(//a[normalize-space()='Anritsu Company'])[1]
${CONTINENTAL}              xpath=(//a[normalize-space()='Anritsu Company'])[1]
${NESS}                     xpath=(//a[normalize-space()='Ness Digital Engineering'])[1]
${BARRA}                    xpath=(//a[normalize-space()='Barra (Co-Owner, Restaurant Business)'])[1]

#Education
${DIMA}                     xpath=(//a[normalize-space()='Industrial Design, and Business Management'])[1]
${ETTI}                     xpath=(//a[contains(text(),'Electrical, Electronics, and Telecommunications En')])[1]
${NEGRUZZI}                 xpath=(//a[normalize-space()='Mathematics and Computer Science Profile'])[1]

# Download CV
${DOWNLOAD CV}              xpath=(//strong[normalize-space()='Download my PDF Curriculum Vitae'])[1]

# Contact Social Media Links
${LINKEDIN}                 xpath=(//a[@href='https://www.linkedin.com/in/tudor-gall'])[1]
${WHATSAPP}                 xpath=(//a[contains(@href,'wa.me/40746677095')])[1]
${GITHUB}                   xpath=(//a[contains(@href,'https://github.com/xgalltudor')])[1]
${FACEBOOK}                 xpath=(//a[contains(@href,'https://www.facebook.com/xgalltudor')])[1]
${INSTAGRAM}                xpath=(//a[contains(@href,'https://instagram.com/xgalltudor')])[1]
${TWITTER}                  xpath=(//a[contains(@href,'https://twitter.com/xgalltudor')])[1]





