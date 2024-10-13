import allure

from data.fake_data import FakeData
from data.urls import URL
from locators.create_account_locators import CreateAccountLocators
from pages.create_account import CreateAccount


@allure.suite("Registration")
class TestCreateAccount:
    @allure.title("Create a new user")
    def test_create_new_account(self, browser):
        page = CreateAccount(browser)
        page.open(URL.CREATE_ACCOUNT)
        page.create_account(first_name=FakeData.first_name(),
                            last_name=FakeData.last_name(),
                            email=FakeData.email(),
                            password="123456789!Qs@",
                            confirmation_password="123456789!Qs@")
        with allure.step("Успешная регистрация"):
            assert page.current_url() == "https://magento.softwaretestingboard.com/customer/account/"
            assert page.get_text(CreateAccountLocators.MESSAGE) == "Thank you for registering with Main Website Store."

    @allure.title("Registration with empty first name field")
    def test_create_account_empty_first_name_field(self, browser):
        page = CreateAccount(browser)
        page.open(URL.CREATE_ACCOUNT)
        page.create_account(first_name=None,
                            last_name=FakeData.last_name(),
                            email=FakeData.email(),
                            password="123456",
                            confirmation_password="123456")
        with allure.step("Error: This is a required field"):
            assert page.get_text(CreateAccountLocators.FIRST_NAME_ERROR) == "This is a required field."

    @allure.title("Password is less than 8 characters")
    def test_create_account_pass_less_8ch(self, browser):
        page = CreateAccount(browser)
        page.open(URL.CREATE_ACCOUNT)
        page.create_account(first_name=FakeData.first_name(),
                            last_name=FakeData.last_name(),
                            email=FakeData.email(),
                            password="1234567",
                            confirmation_password="1234567")
        with allure.step("Error message"):
            assert page.get_text(CreateAccountLocators.PASSWORD_ERROR) == ("Minimum length of this field must be equal "
                                                                           "or greater than 8 symbols. Leading and "
                                                                           "trailing spaces will be ignored.")

    @allure.title("Create an account with not match passwords")
    def test_create_account_not_match_passwords(self, browser):
        page = CreateAccount(browser)
        page.open(URL.CREATE_ACCOUNT)
        page.create_account(first_name=FakeData.first_name(),
                            last_name=FakeData.last_name(),
                            email=FakeData.email(),
                            password="12@69Q8w24",
                            confirmation_password="123")

        with allure.step("Error: Please enter the same value again"):
            assert page.get_text(CreateAccountLocators.CONFIRM_PASSWORD_ERROR) == "Please enter the same value again."
