import pytest
from selenium import webdriver
import logging
from test_resources.test_keywords import Keywords
from test_resources.test_variables import Locators

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="module")
def setup_teardown():
    driver = webdriver.Chrome()
    keywords = Keywords(driver, logger)
    keywords.open_site()

    yield keywords  # Provide fixture value

    driver.quit()

# Test cases


def test_navigate_to_home_page(setup_teardown):
    keywords = setup_teardown
    keywords.user_is_on_home_page()


def test_click_on_about_me_upper_button(setup_teardown):
    keywords = setup_teardown
    keywords.click_element(Locators.about_me_upper_button_xpath)
    keywords.user_is_on_about_me_page()


def test_click_on_cv_upper_button(setup_teardown):
    keywords = setup_teardown
    keywords.click_element(Locators.cv_upper_button_xpath)
    keywords.user_is_on_cv_page()


def test_click_on_contact_upper_button(setup_teardown):
    keywords = setup_teardown
    keywords.click_element(Locators.contact_upper_button_xpath)
    keywords.user_is_on_contact_page()


def test_click_on_home_upper_button(setup_teardown):
    keywords = setup_teardown
    keywords.click_element(Locators.home_upper_button_xpath)
    keywords.user_is_on_home_page()


def test_click_on_about_me_lower_button(setup_teardown):
    keywords = setup_teardown
    keywords.click_element(Locators.about_me_lower_button_xpath)
    keywords.user_is_on_about_me_page()


def test_click_on_cv_lower_button(setup_teardown):
    keywords = setup_teardown
    keywords.click_element(Locators.cv_lower_button_xpath)
    keywords.user_is_on_cv_page()


def test_click_on_contact_lower_button(setup_teardown):
    keywords = setup_teardown
    keywords.click_element(Locators.contact_lower_button_xpath)
    keywords.user_is_on_contact_page()


def test_click_on_home_lower_button(setup_teardown):
    keywords = setup_teardown
    keywords.click_element(Locators.home_lower_button_xpath)
    keywords.user_is_on_home_page()
