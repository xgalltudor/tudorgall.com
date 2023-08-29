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
    k = Keywords(driver, logger)
    k.open_site()
    yield k
    driver.quit()


def test_navigate_to_cv_page_and_check_pdf_downloads(setup_teardown):
    k = setup_teardown

    k.user_is_on_home_page()
    k.click_element(Locators.cv_upper_button_xpath)
    k.user_is_on_cv_page()
    k.verify_pdf_opens_in_new_tab()