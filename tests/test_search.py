import allure

from data.urls import URL
from locators.item_locators import ItemLocators
from pages.search_page import Search


@allure.suite("Search")
class TestSearch:
    @allure.title("Search by 2 characters")
    def test_search_for_2_simbols(self, browser):
        page = Search(browser)
        page.open(URL.MAIN_MAIGE)
        page.send_search_field("ac")
        page.send_enter()
        with allure.step("Error: Minimum Search query"):
            assert "Minimum Search query length is 3" in page.search_results_message()

    @allure.title("Search by 3 characters")
    def test_search_for_3_simbols(self, browser):
        page = Search(browser)
        page.open(URL.MAIN_MAIGE)
        page.send_search_field("jac")
        page.send_enter()
        with allure.step("There are products on the search results page"):
            assert len(ItemLocators.MINI_ITEMS) > 0

    @allure.title("Search for a non-existent product")
    def test_search_for_non_exist_product(self, browser):
        page = Search(browser)
        page.open(URL.MAIN_MAIGE)
        page.send_search_field("mom")
        page.send_enter()
        with allure.step("Error message: 'Your search returned no results'"):
            assert "Your search returned no results." in page.search_results_message()

    @allure.title("Product search by full name")
    def test_search_for_full_product_name(self, browser):
        page = Search(browser)
        page.open(URL.MAIN_MAIGE)
        page.send_search_field("Ina Compression Short")
        page.send_enter()
        with allure.step("Product is found"):
            assert page.find_elem_by_name_in_results(name="Ina Compression Short")

    @allure.title("Product search by partial coincidence")
    def test_search_for_partial_coincidence_name(self, browser):
        page = Search(browser)
        page.open(URL.MAIN_MAIGE)
        page.send_search_field("jacket")
        page.send_enter()
        with allure.step("Product is found"):
            assert page.find_elem_by_name_in_results(name="Jacket")
