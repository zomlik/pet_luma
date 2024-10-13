import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()
pytest_plugins = ["fixtures.account"]


def pytest_addoption(parser):
    """Пользовательские опции командной строки"""
    parser.addoption("--ci", action='store', default="true")


@pytest.fixture()
def chrome_options(request):
    options = Options()
    if request.config.getoption("ci") == "true":
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    return options


@pytest.fixture()
def browser(chrome_options):
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
