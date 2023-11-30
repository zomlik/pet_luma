from base.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def find_logo(self):
        return self.is_visible(MainPageLocators.LOGO)
