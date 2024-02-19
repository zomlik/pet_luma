import allure
from data.urls import URL
from data.fake_data import FakeData
from pages.create_account import CreateAccount
from locators.create_account_locators import CreateAccountLocators


@allure.suite("Регистрация")
class TestCreateAccount(FakeData):
    @allure.title("Регистрация нового пользователя")
    def test_create_account(self, browser):
        page = CreateAccount(browser)
        page.open(URL.CREATE_ACCOUNT)
        page.send_first_name(self.first_name())
        page.send_last_name(self.last_name())
        page.send_email(self.email())
        page.send_password("123456789!Qs@")
        page.send_confirmation_password("123456789!Qs@")
        with allure.step("Сообщение об успешной регистрации"):
            assert page.get_text(CreateAccountLocators.H1_MY_ACCOUNT) == "My Account"

    @allure.title("Регистрация с не заполненным полем First Name")
    def test_create_account_empty_first_name_field(self, browser):
        page = CreateAccount(browser)
        page.open(URL.CREATE_ACCOUNT)
        page.send_last_name(self.first_name())
        page.send_email(self.email())
        page.send_password("123456789!2Qs")
        page.send_confirmation_password("123456789!2Qs")
        page.click_button()
        with allure.step("Сообщение об ошибке This is a required field"):
            assert page.get_text(CreateAccountLocators.FIRST_NAME_ERROR) == "This is a required field."

    @allure.title("Пароль менее 8 символов")
    def test_create_account_empty_email_field(self, browser):
        page = CreateAccount(browser)
        page.open(URL.CREATE_ACCOUNT)
        page.send_first_name(self.first_name())
        page.send_last_name(self.last_name())
        page.send_email(self.email())
        page.send_password("!2sQ5")
        page.send_confirmation_password("!2sQ5")
        page.click_button()
        with allure.step("Сообщение об ошибке"):
            assert page.get_text(CreateAccountLocators.PASSWORD_ERROR) == ("Minimum length of this field must be equal "
                                                                           "or greater than 8 symbols. Leading and "
                                                                           "trailing spaces will be ignored.")

    @allure.title("Не совподение паролей при регистрации")
    def test_create_account_not_match_passwords(self, browser):
        page = CreateAccount(browser)
        page.open(URL.CREATE_ACCOUNT)
        page.send_first_name(self.first_name())
        page.send_last_name(self.last_name())
        page.send_email(self.email())
        page.send_password("12@69Q8w24")
        page.send_confirmation_password("123")
        page.click_button()
        with allure.step("Сообщение об ошибке Please enter the same value again"):
            assert page.get_text(CreateAccountLocators.CONFIRM_PASSWORD_ERROR) == "Please enter the same value again."
