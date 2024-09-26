import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://saucedemo.com')
    driver.maximize_window()

    yield driver

    driver.quit()