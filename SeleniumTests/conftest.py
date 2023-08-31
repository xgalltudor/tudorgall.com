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
    service = Service(executable_path='/usr/local/bin/chromedriver')
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome-stable"
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    keywords = Keywords(driver, logger)
    keywords.open_site()

    yield keywords

    driver.quit()
