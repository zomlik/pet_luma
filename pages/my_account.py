from base.base_page import BasePage
from locators.my_account_locators import MyAccountLocators


class MyAccount(BasePage):
    def switch_button(self):
        return self.is_clickable(MyAccountLocators.SWITCH_BUTTON).click()
