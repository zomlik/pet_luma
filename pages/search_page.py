import allure
from base.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.search_results_locatators import SearchResultsLocators


class Search(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Поиск")
    def send_search_field(self, keys: str):
        return self.is_visible(MainPageLocators.SEARCH_BOX).send_keys(keys)

    def search_results_message(self):
        return self.get_text(SearchResultsLocators.SEARCH_MESSAGE_ERROR)
