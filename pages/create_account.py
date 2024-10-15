import allure

from base.base_page import BasePage
from locators.create_account_locators import CreateAccountLocators


class CreateAccount(BasePage):
    def create_account(self,
                       first_name: str,
                       last_name: str,
                       email: str,
                       password: str,
                       confirmation_password: str):
        with allure.step("Fill first name field"):
            self.is_visible(CreateAccountLocators.FIRST_NAME).send_keys(first_name)
        with allure.step("Fill last name field"):
            self.is_visible(CreateAccountLocators.LAST_NAME).send_keys(last_name)
        with allure.step("Fill email field"):
            self.is_visible(CreateAccountLocators.EMAIL).send_keys(email)
        with allure.step("Fill password field"):
            self.is_visible(CreateAccountLocators.PASSWORD).send_keys(password)
        with allure.step("Fill confirm password field"):
            self.is_visible(CreateAccountLocators.CONFIRM_PASSWORD).send_keys(confirmation_password)
        with allure.step("Click on Create an account button"):
            self.is_clickable(CreateAccountLocators.CREATE_ACCOUNT_BUTTON).click()

    @staticmethod
    def error_required():
        return "This is a required field."
