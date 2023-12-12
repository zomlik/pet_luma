import allure
from base.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Лого отображается на странице")
    def logo_is_visible(self):
        return self.is_visible(MainPageLocators.LOGO)

    @allure.step("Поисковая строка отображается на странице")
    def search_box_is_visible(self):
        return self.find(MainPageLocators.SEARCH_BOX)

    @allure.step("Получение атрибута placeholder поисковой строки")
    def search_box_placeholder(self):
        return self.find(MainPageLocators.SEARCH_BOX).get_attribute("placeholder")

    @allure.step("Кнопка поиска отобрадается на странице")
    def search_box_button_is_visible(self):
        return self.is_visible(MainPageLocators.SEARCH_BOX_BUTTON)

