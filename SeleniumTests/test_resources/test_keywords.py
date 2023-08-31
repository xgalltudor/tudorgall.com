from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_resources.test_variables import Locators
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time


class Keywords:
    """This class contains various utility methods for interacting with a web application."""

    def __init__(self, driver, logger):
        """
        Initializes the Keywords class with a Selenium WebDriver instance and a logger.

        Parameters:
            - driver (WebDriver): Selenium WebDriver instance.
            - logger (Logger): Logging object for reporting.
        """
        self.driver = driver
        self.logger = logger

    def open_site(self):
        """Opens the website and maximizes the window."""
        self.driver.get(Locators.url)
        self.driver.maximize_window()
        self.logger.info(f"Opened {Locators.url}")

    def click_element(self, element):
        """Clicks an element given a xpath"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, element))).click()

    def element_is_displayed(self, element):
        """Element is displayed given a xpath. Returns True if displayed, otherwise False."""
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
            return True
        except TimeoutException:
            return False

    def element_input_text(self, element, input):
        """Inputs text given a xpath element"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element))).send_keys(input)

    def element_text(self, element):
        """Retrieves the text attribute of an element"""
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element))).text

    def navigate_to_page(self, page):
        """
        Navigates to the specified page on the website.

        Parameters:
            - page (str): The name of the page to navigate to.
        """
        url_slug = Locators.page_urls[page]
        self.driver.get(f"{Locators.url}/{url_slug}")
        self.logger.info(f"Navigated to page{page}")

    def check_page_title(self, title):
        """
        Checks if the current page title matches the expected title.

        Parameters:
            - title (str): The expected title of the page.
        """
        time.sleep(1)
        assert title == self.driver.title, f"{title} does not match {self.driver.title}"
        self.logger.info(f"Title {title} matches")

    def page_contains_upper_and_lower_buttons(self):
        """Verifies that the page contains the expected upper and lower navigation buttons."""
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
        """Verifies that the home page contains all the expected inner elements."""
        elements = [
            Locators.lets_talk_button_xpath,
            Locators.contact_me_button_xpath,
            Locators.main_skills_xpath
        ]
        for element in elements:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        self.logger.info("Home page contains inner elements")

    def about_me_page_contains_inner_elements(self):
        """Verifies that the About Me page contains all the expected inner elements."""
        elements = [Locators.contact_me_button_xpath]
        for element in elements:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        self.logger.info("About me page contains inner elements")

    def cv_page_contains_inner_elements(self):
        """Verifies that the CV page contains all the expected inner elements."""
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
        """Verifies that the Contact page contains all the expected inner elements."""
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

    def user_is_on_home_page(self):
        """Verifies that the user is currently on the home page by checking the title and essential elements."""
        time.sleep(1)
        self.check_page_title(Locators.home_title)
        self.page_contains_upper_and_lower_buttons()
        self.home_page_contains_inner_elements()
        self.logger.info("User is on Home page")

    def user_is_on_about_me_page(self):
        """Verifies that the user is currently on the About Me page by checking the title and essential elements."""
        time.sleep(1)
        self.check_page_title(Locators.about_me_title)
        self.page_contains_upper_and_lower_buttons()
        self.about_me_page_contains_inner_elements()
        self.logger.info("User is on About me page")

    def user_is_on_cv_page(self):
        """Verifies that the user is currently on the CV page by checking the title and essential elements."""
        time.sleep(1)
        self.check_page_title(Locators.cv_title)
        self.page_contains_upper_and_lower_buttons()
        self.cv_page_contains_inner_elements()
        self.logger.info("User is on CV page")

    def user_is_on_contact_page(self):
        """Verifies that the user is currently on the Contact page by checking the title and essential elements."""
        time.sleep(1)
        self.check_page_title(Locators.contact_title)
        self.page_contains_upper_and_lower_buttons()
        self.contact_page_contains_inner_elements()
        self.logger.info("User is on Contact page")

    def switch_to_new_tab(self):
        """Switches the driver's context to the last opened tab."""

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.logger.info("Switched to new tab")

    def verify_pdf_cv(self, expected_url=Locators.cv_pdf_url):
        """Verifies that a PDF has the correct link when the user clicks the 'Download my PDF Curriculum Vitae' link."""

        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.download_cv_xpath)))
        actual_url = element.get_attribute('href')
        print("Actual URL: ", actual_url)
        print("Expected URL: ", expected_url)
        assert actual_url == expected_url, "URLs do not match"
        self.logger.info(f"CV element {element} has the correct URL: {expected_url}")

        target_value = element.get_attribute('target')
        assert target_value == "_blank", "Link does not open in new tab"


    def verify_social_media_link_opens_in_new_tab(self, element_locator, expected_url):
        """
        Verifies that clicking on a social media link opens the correct URL in a new tab.

        Parameters:
            - element_locator (str): The XPATH locator for the social media element.
            - expected_url (str): The expected URL that should be opened in a new tab.
        """

        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_locator)))
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
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.logger.info("Successfully switched to new tab")
        self.driver.close()
        self.logger.info("Closed the new tab")

        original_handle = all_handles[0]
        self.driver.switch_to.window(original_handle)
        self.logger.info("Switched back to the original tab")

    def verify_email_or_phone_link(self, element_locator, expected_url):
        """
        Verifies that the email or phone link is correct.

        Parameters:
            - element_locator (str): The XPATH locator for the email or phone element.
            - expected_url (str): The expected 'mailto' or 'tel' URL.
        """

        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_locator)))
        actual_url = element.get_attribute('href')
        assert actual_url == expected_url, "URLs do not match"
        self.logger.info(f"Email/Phone element {element_locator} has the correct URL: {expected_url}")


