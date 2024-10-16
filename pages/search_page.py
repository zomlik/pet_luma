import allure

from base.base_page import BasePage
from locators.item_locators import ItemLocators
from locators.main_page_locators import MainPageLocators
from locators.search_results_locatators import SearchResultsLocators


class Search(BasePage):
    @allure.step("Fill search box")
    def send_search_field(self, keys: str):
        return self.is_visible(MainPageLocators.SEARCH_BOX).send_keys(keys)

    def search_results_message(self):
        return self.get_text(SearchResultsLocators.SEARCH_MESSAGE_ERROR)

    def find_elem_by_name_in_results(self, name: str):
        elems = self.all_elems_is_visibles(ItemLocators.MINI_ITEMS_NAME)
        for item in elems:
            if name in item.text:
                return True
            else:
                return False
