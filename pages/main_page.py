from base.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def logo_is_visible(self):
        return self.is_visible(MainPageLocators.LOGO)

    def search_box_is_visible(self):
        return self.find(MainPageLocators.SEARCH_BOX)

    def search_box_placeholder(self):
        return self.find(MainPageLocators.SEARCH_BOX).get_attribute("placeholder")

    def search_box_button_is_visible(self):
        return self.is_visible(MainPageLocators.SEARCH_BOX_BUTTON)
