import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
