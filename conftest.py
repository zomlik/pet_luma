import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pytest_plugins = ["fixtures.account"]


@pytest.fixture()
def chrome_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    return options


@pytest.fixture()
def browser(chrome_options):
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
