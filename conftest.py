import allure
import pytest
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()
pytest_plugins = ["fixtures.account"]


def pytest_addoption(parser):
    """Custom Command Line options"""
    parser.addoption("--ci", action='store', default="true")


@pytest.fixture()
def chrome_options(request):
    """Chrome options"""
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Attach screenshots to allure report"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        browser = item.funcargs["browser"]
        allure.attach(browser.get_screenshot_as_png(),
                      name=f"Screenshot {datetime.now()}",
                      attachment_type=allure.attachment_type.PNG)
