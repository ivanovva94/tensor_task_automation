import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
