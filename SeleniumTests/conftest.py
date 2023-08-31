import pytest
import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from test_resources.test_keywords import Keywords

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="module")
def setup_teardown():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.implicitly_wait(5)
    keywords = Keywords(driver, logger)
    keywords.open_site()

    yield keywords

    driver.quit()
