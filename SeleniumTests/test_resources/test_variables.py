class Locators:
    # URL & Browser
    url = "https://www.tudorgall.com"
    browser = "Chrome"

    # URL Slugs
    home = "home"
    about_me = "about"
    contact = "contact"
    cv = "curriculum-vitae"
    page_urls = {
        "Home": "",
        "About me": "about",
        "CV": "curriculum-vitae",
        "Contact": "contact"
    }

    # Titles
    home_title = "Tudor Gall – Test Automation Developer"
    about_me_title = "About me – Tudor Gall"
    cv_title = "Curriculum Vitae – Tudor Gall"
    contact_title = "Contact – Tudor Gall"

    # Upper & Lower Buttons
    home_upper_button_xpath = "(//a[normalize-space()='Home'])[1]"
    home_lower_button_xpath = "(//a[normalize-space()='Home'])[2]"
    about_me_upper_button_xpath = "(//a[normalize-space()='About me'])[1]"
    about_me_lower_button_xpath = "(//a[normalize-space()='About me'])[2]"
    cv_upper_button_xpath = "(//a[normalize-space()='Curriculum Vitae'])[1]"
    cv_lower_button_xpath = "(//a[normalize-space()='Curriculum Vitae'])[2]"
    contact_upper_button_xpath = "(//a[normalize-space()='Contact'])[1]"
    contact_lower_button_xpath = "(//a[normalize-space()='Contact'])[2]"

    # Tudor Gall Home Redirect Buttons
    tg_main_button_xpath = "(//a[normalize-space()='Tudor Gall'])[1]"
    tg_secondary_button_xpath = "(//a[@class='site-name'])[1]"

    # Inner elements
    lets_talk_button_xpath = "(//a[contains(text(),'Let’s talk!')])[1]"
    contact_me_button_xpath = "(//a[normalize-space()='Contact me'])[1]"
    submit_button_xpath = "(//button[normalize-space()='Submit'])[1]"
    main_skills_xpath = "(//a[normalize-space()='Main skills'])[1]"

    # Companies
    anritsu_xpath = "(//a[normalize-space()='Anritsu Company'])[1]"
    continental_xpath = "(//a[normalize-space()='Anritsu Company'])[1]"
    ness_xpath = "(//a[normalize-space()='Ness Digital Engineering'])[1]"
    barra_xpath = "(//a[normalize-space()='Barra (Co-Owner, Restaurant Business)'])[1]"

    # Education
    dima_xpath = "(//a[normalize-space()='Industrial Design, and Business Management'])[1]"
    etti_xpath = "(//a[contains(text(),'Electrical, Electronics, and Telecommunications En')])[1]"
    negruzzi_xpath = "(//a[normalize-space()='Mathematics and Computer Science Profile'])[1]"

    # Download CV
    download_cv_xpath = "(//strong[normalize-space()='Download my PDF Curriculum Vitae'])"

    # Contact Social Media Links
    linkedin_xpath = "(//a[@href='https://www.linkedin.com/in/tudor-gall'])[1]"
    whatsapp_xpath = "(//a[contains(@href,'wa.me/40746677095')])[1]"
    github_xpath = "(//a[contains(@href,'https://github.com/xgalltudor')])[1]"
    facebook_xpath = "(//a[contains(@href,'https://www.facebook.com/xgalltudor')])[1]"
    instagram_xpath = "(//a[contains(@href,'https://instagram.com/xgalltudor')])[1]"
    twitter_xpath = "(//a[contains(@href,'https://twitter.com/xgalltudor')])[1]"

    linkedin_url = "https://www.linkedin.com/in/tudor-gall"
    whatsapp_url = "https://wa.me/40746677095"
    github_url = "https://github.com/xgalltudor"
    facebook_url = "https://www.facebook.com/xgalltudor"
    instagram_url = "https://instagram.com/xgalltudor"
    twitter_url = "https://twitter.com/xgalltudor"

    # Contact info
    yahoo_mail_xpath = "(//a[normalize-space()='xgalltudor@yahoo.com'])[1]"
    google_mail_xpath = "(//a[normalize-space()='xgalltudor23@gmail.com'])[1]"
    phone_number_xpath = "(//a[normalize-space()='+40 746 677 095'])[1]"

    yahoo_mail_link = "mailto:xgalltudor@yahoo.com"
    google_mail_link = "mailto:xgalltudor23@gmail.com"
    phone_number_link = "tel:+40746677095"

    # Download Directory Path
    cv_pdf_url = "https://tudorgall.files.wordpress.com/2023/08/tudor-galls-cv.pdf"

    # Contact fields
    contact_name_xpath = "(//input[@id='g36-name'])[1]"
    contact_email_xpath = "(//input[@id='g36-email'])[1]"
    contact_message_xpath = "(//textarea[@id='contact-form-comment-g36-tellmemore'])[1]"
    contact_phone_xpath = "(//input[@id='g36-phone'])[1]"

    # Dummy contact details
    name_input = "Spamiel Spamilton"
    email_input = "spam@spamail.com"
    message_input = "Hello Tudor! This is a SPAM message from 'TC005 - Submit a Contact Message.robot'"
    phone_input = "0740000000"

    # Message sent confirmation
    message_sent_xpath = "(//h4[normalize-space()='Your message has been sent'])[1]"
    message_sent_text = "Your message has been sent"
