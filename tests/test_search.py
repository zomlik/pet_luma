import allure
from pages.search_page import Search
from locators.search_results_locatators import SearchResultsLocators
from locators.item_locators import ItemLocators
from data.urls import URL


@allure.title("PL-7 Поиск по 2 символам")
def test_search_for_2_simbols(browser):
    page = Search(browser)
    page.open(URL.BASE_URL)
    page.send_search_field("ac")
    page.send_enter()
    with allure.step("Проверка, что минемальная длинна 3 символа"):
        assert "Minimum Search query length is 3" in page.search_results_message()


@allure.title("PL-8 Поиск по 3 символам")
def test_search_for_3_simbols(browser):
    page = Search(browser)
    page.open(URL.BASE_URL)
    page.send_search_field("jac")
    page.send_enter()
    with allure.step("На странице с результатами поиска присутствуют товары"):
        assert len(ItemLocators.MINI_ITEMS) > 0
