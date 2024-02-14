import allure
from base.base_page import BasePage
from locators.create_account_locators import CreateAccountLocators


class CreateAccount(BasePage):
    @allure.step("Поле First Name")
    def send_first_name(self, first_name: str):
        return self.is_visible(CreateAccountLocators.FIRST_NAME).send_keys(first_name)

    @allure.step("Поле Last Name")
    def send_last_name(self, last_name: str):
        return self.is_visible(CreateAccountLocators.LAST_NAME).send_keys(last_name)

    @allure.step("Поле Email")
    def send_email(self, email: str):
        return self.is_visible(CreateAccountLocators.EMAIL).send_keys(email)

    @allure.step("Поле Password")
    def send_password(self, password: str):
        return self.is_visible(CreateAccountLocators.PASSWORD).send_keys(password)

    @allure.step("Поле Confirmation Password")
    def send_confirmation_password(self, confirmation_password: str):
        return self.is_visible(CreateAccountLocators.CONFIRM_PASSWORD).send_keys(confirmation_password)

    @allure.step("Клик по кнопке Create An Account")
    def click_button(self):
        return self.is_visible(CreateAccountLocators.CREATE_ACCOUNT_BUTTON).click()

