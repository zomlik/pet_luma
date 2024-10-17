import allure
import os

from data.fake_data import FakeData
from data.urls import URL
from pages.sing_in import SingIn


@allure.suite("Login In")
class TestSingIn(FakeData):
    @allure.title("Login In")
    def test_sing_in(self, browser):
        page = SingIn(browser)
        page.open(URL.LOGIN_PAGE)
        page.sing_in(email=os.environ["EMAIL"], password=os.environ["PASSWORD"])
        with allure.step("Successful authorization message"):
            assert "Welcome" in page.welcome_message()

    @allure.title("Login in with empty email field")
    def test_empty_email_field(self, browser):
        page = SingIn(browser)
        page.sing_in(email="", password="123456")
        with allure.step("Error: This is a required field"):
            assert page.email_errors_messages() == "This is a required field."

    @allure.title("Login in with empty password field")
    def test_empty_password_field(self, browser):
        page = SingIn(browser)
        page.open(URL.LOGIN_PAGE)
        page.sing_in(email=os.getenv("EMAIL"), password="")
        with allure.step("Error: This is a required field"):
            assert page.pass_errors_messages() == "This is a required field."

    @allure.title("Click on button Create an Account")
    def test_click_create_account_button(self, browser):
        page = SingIn(browser)
        page.open(URL.LOGIN_PAGE)
        page.click_create_account_button()
        with allure.step("Open registration page"):
            assert page.current_url() == URL.CREATE_ACCOUNT

    @allure.title("Click on forgot password link")
    def test_click_forgot_password_link(self, browser):
        page = SingIn(browser)
        page.open(URL.LOGIN_PAGE)
        page.click_forgot_password_link()
        with allure.step("Open forgot password page"):
            assert page.current_url() == URL.FORGOT_PASSWORD
