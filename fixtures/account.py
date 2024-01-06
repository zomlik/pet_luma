import pytest
from locators.login_page_locators import LoginPageLocator
from data.urls import URL


@pytest.fixture()
def sing_in(browser):
    browser.get(URL.LOGIN_PAGE)
    browser.find_element(*LoginPageLocator.EMAIL_FIELD).send_keys("facesod700@vasteron.com")
    browser.find_element(*LoginPageLocator.PASSWORD).send_keys("TestMyPassword25")
    browser.find_element(*LoginPageLocator.SING_IN_BUTTON).click()
