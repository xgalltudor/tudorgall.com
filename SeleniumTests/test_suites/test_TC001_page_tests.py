import pytest
from selenium import webdriver
import logging
from test_resources.test_keywords import Keywords

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="module")
def setup_teardown():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    keywords = Keywords(driver, logger)
    keywords.open_site()

    yield keywords  # Provide fixture value

    driver.quit()


def test_navigate_directly_to_home_page(setup_teardown):
    keywords = setup_teardown
    keywords.navigate_to_page("Home")
    keywords.user_is_on_home_page()


def test_navigate_directly_to_about_me_page(setup_teardown):
    keywords = setup_teardown
    keywords.navigate_to_page("About me")
    keywords.user_is_on_about_me_page()


def test_navigate_directly_to_curriculum_vitae_page(setup_teardown):
    keywords = setup_teardown
    keywords.navigate_to_page("CV")
    keywords.user_is_on_cv_page()


def test_navigate_directly_to_contact_page(setup_teardown):
    keywords = setup_teardown
    keywords.navigate_to_page("Contact")
    keywords.user_is_on_contact_page()
