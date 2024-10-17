import pytest
import os
import allure

from data.urls import URL
from pages.sing_in import SingIn


@pytest.fixture()
@allure.step("Sing in")
def sing_in(browser):
    page = SingIn(browser)
    page.open(URL.LOGIN_PAGE)
    page.sing_in(email=os.environ["EMAIL"], password=os.environ["PASSWORD"])
