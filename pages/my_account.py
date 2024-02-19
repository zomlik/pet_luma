from base.base_page import BasePage
from locators.my_account_locators import MyAccountLocators


class MyAccount(BasePage):
    def swith_battun(self):
        return self.is_clickable(MyAccountLocators.SWITH_BUTTON).click()
