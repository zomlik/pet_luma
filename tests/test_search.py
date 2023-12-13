import allure
from pages.search_page import Search
from data.urls import URL


@allure.title("PL-7 Поиск по 2 символам")
def test_search_for_2_simbols(browser):
    page = Search(browser)
    page.open(URL.BASE_URL)
    page.send_search_field("ac")
    page.send_enter()
    with allure.step("Проверка, что минемальная длинна 3 символа"):
        assert "Minimum Search query length is 3" in page.search_results_message()
