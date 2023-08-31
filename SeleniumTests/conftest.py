import pytest
import logging
import os
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from test_resources.test_keywords import Keywords

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="function")
def setup_teardown(request):
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

    if request.node.rep_call.failed:
        take_screenshot(driver, request.node.name)

    driver.quit()

def take_screenshot(driver, testcase):
    now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file = os.path.join(os.environ.get('PYTHONPATH', '.'), f'screenshot_{testcase}_{now}.png')
    try:
        driver.get_screenshot_as_file(file)
        logger.info(f"\n\nScreenshot taken: {file}\n\n")
    except WebDriverException as e:
        logger.info(f'Could not take a screenshot because of exception: {e}')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
