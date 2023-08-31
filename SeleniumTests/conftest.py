import pytest
import logging
import time
from datetime import datetime
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, setup_teardown):
    yield
    if request.node.rep_call.failed:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        setup_teardown.save_screenshot(f"screenshot_{now}.png")