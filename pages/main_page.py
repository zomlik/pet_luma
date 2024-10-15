import allure

from base.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Click on logo")
    def click_on_logo(self):
        return self.is_visible(MainPageLocators.LOGO).click()

    @allure.step("Search box")
    def search_box_is_visible(self):
        return self.is_visible(MainPageLocators.SEARCH_BOX)

    @allure.step("Getting an attribute placeholder for search box")
    def search_box_placeholder(self):
        return self.is_visible(MainPageLocators.SEARCH_BOX).get_attribute("placeholder")

    @allure.step("Search button")
    def search_box_button_is_visible(self):
        return self.is_visible(MainPageLocators.SEARCH_BOX_BUTTON)

    @allure.step("Click on the cart")
    def click_cart(self):
        return self.is_clickable(MainPageLocators.CART_ICON).click()

    @allure.step("Empty cart message")
    def cart_empty_message(self):
        return self.get_text(MainPageLocators.CART_EMPTY_MESSAGE)
