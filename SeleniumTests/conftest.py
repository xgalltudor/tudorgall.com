import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()