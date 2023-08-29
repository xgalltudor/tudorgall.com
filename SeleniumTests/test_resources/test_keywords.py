from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_resources.test_variables import Locators
from selenium import webdriver


class Keywords:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def open_site(self):
        self.driver.get(Locators.url)
        self.driver.maximize_window()
        self.logger.info(f"Opened {Locators.url}")

    def navigate_to_page(self, page):
        url_slug = Locators.page_urls[page]
        self.driver.get(f"{Locators.url}/{url_slug}")
        self.logger.info(f"Navigated to page{page}")

    def check_page_title(self, title):
        assert title == self.driver.title, f"{title} does not match {self.driver.title}"
        self.logger.info(f"Title {title} matches")

    def page_contains_upper_and_lower_buttons(self):
        elements = [
            Locators.home_upper_button_xpath,
            Locators.about_me_upper_button_xpath,
            Locators.cv_upper_button_xpath,
            Locators.contact_upper_button_xpath,
            Locators.home_lower_button_xpath,
            Locators.about_me_lower_button_xpath,
            Locators.cv_lower_button_xpath,
            Locators.contact_lower_button_xpath,
            Locators.tg_main_button_xpath,
            Locators.tg_secondary_button_xpath
        ]
        for element in elements:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        self.logger.info("Page contains upper and lower buttons")

    def home_page_contains_inner_elements(self):
        elements = [
            Locators.lets_talk_button_xpath,
            Locators.contact_me_button_xpath,
            Locators.main_skills_xpath
        ]
        for element in elements:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        self.logger.info("Home page contains inner elements")

    def about_me_page_contains_inner_elements(self):
        elements = [Locators.contact_me_button_xpath]
        for element in elements:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        self.logger.info("About me page contains inner elements")

    def cv_page_contains_inner_elements(self):
        elements = [
            Locators.contact_me_button_xpath,
            Locators.anritsu_xpath,
            Locators.continental_xpath,
            Locators.ness_xpath,
            Locators.barra_xpath,
            Locators.dima_xpath,
            Locators.etti_xpath,
            Locators.negruzzi_xpath,
            Locators.download_cv_xpath
        ]
        for element in elements:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        self.logger.info("CV page contains inner elements")

    def contact_page_contains_inner_elements(self):
        elements = [
            Locators.linkedin_xpath,
            Locators.whatsapp_xpath,
            Locators.github_xpath,
            Locators.facebook_xpath,
            Locators.instagram_xpath,
            Locators.twitter_xpath,
            Locators.submit_button_xpath
        ]
        for element in elements:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        self.logger.info("Contact page contains inner elements")

    # User is on Home Page
    def user_is_on_home_page(self):
        self.check_page_title(Locators.home_title)
        self.page_contains_upper_and_lower_buttons()
        self.home_page_contains_inner_elements()

    # User is on Home Page
    def user_is_on_about_me_page(self):
        self.check_page_title(Locators.about_me_title)
        self.page_contains_upper_and_lower_buttons()
        self.about_me_page_contains_inner_elements()

    # User is on CV Page
    def user_is_on_cv_page(self):
        self.check_page_title(Locators.cv_title)
        self.page_contains_upper_and_lower_buttons()
        self.cv_page_contains_inner_elements()

    # User is on Contact Page
    def user_is_on_contact_page(self):
        self.check_page_title(Locators.contact_title)
        self.page_contains_upper_and_lower_buttons()
        self.contact_page_contains_inner_elements()

    # Function to switch to a new tab
    def switch_to_new_tab(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    # Verify PDF Opens in New Tab when the User clicks on "Download my PDF Curriculum Vitae"
    def verify_pdf_opens_in_new_tab(self):
        main_window = self.driver.window_handles
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.download_cv_xpath))).click()
        self.switch_to_new_tab()
        current_url = self.driver.get.current(Locators.cv_pdf_url)

    # Verify Social Media Link Opens In New Tab
    def verify_social_media_link_opens_in_new_tab(self, element_locator, expected_url):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_locator)))
        element = self.driver.find_element_by_xpath(element_locator)
        actual_url = element.get_attribute('href')
        assert actual_url == expected_url, "URLs do not match"
        self.logger.info(f"Social Medial element {element_locator} has the correct URL: {expected_url}")

        target_value = element.get_attribute('target')
        assert target_value == "_blank", "Link does not open in new tab"

        element.click()
        self.logger.info(f"Clicked on {element_locator}")

        all_handles = self.driver.window_handles
        new_handle = all_handles[-1]
        self.driver.switch_to.window(new_handle)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tag:body")))
        self.logger.info("Successfully switched to new tab")
        self.driver.close()
        self.logger.info("Closed the new tab")

        original_handle = all_handles[0]
        self.driver.switch_to.window(original_handle)
        self.logger.info("Switched back to the original tab")

    # Verify email or phone link
    def verify_email_or_phone_link(self, element_locator, expected_url):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_locator)))
        element = self.driver.find_element_by_xpath(element_locator)
        actual_url = element.get_attribute('href')
        assert actual_url == expected_url, "URLs do not match"
        self.logger.info(f"Email/Phone element {element_locator} has the correct URL: {expected_url}")


