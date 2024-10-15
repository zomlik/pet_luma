import allure

from base.base_page import BasePage
from locators.sing_in_locators import SingInLocators


class SingIn(BasePage):
    def sing_in(self, email: str, password: str):
        with allure.step("Fill email field"):
            self.is_visible(SingInLocators.EMAIL).send_keys(email)
        with allure.step("Fill password field"):
            self.is_visible(SingInLocators.PASSWORD).send_keys(password)
        with allure.step("Click on Sing In button"):
            self.is_clickable(SingInLocators.SING_IN_BUTTON).click()

    @allure.step("Click on Create an Account button")
    def click_create_account_button(self):
        return self.is_clickable(SingInLocators.CREATE_ACCOUNT_BUTTON).click()

    @allure.step("Click on Forgot My Password button")
    def click_forgot_password_link(self):
        return self.is_clickable(SingInLocators.FORGOT_PASSWORD_LINK).click()

    def email_errors_messages(self):
        return self.get_text(SingInLocators.EMAIL_ERROR)

    def pass_errors_messages(self):
        return self.get_text(SingInLocators.PASSWORD_ERROR)

    def welcome_message(self):
        return self.get_text(SingInLocators.WELCOME_MESSAGE)
