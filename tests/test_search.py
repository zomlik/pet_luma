import allure
from pages.search_page import Search
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


@allure.title("PL-10 Поиск несуществующего товара")
def test_search_for_non_exist_product(browser):
    page = Search(browser)
    page.open(URL.BASE_URL)
    page.send_search_field("mom")
    page.send_enter()
    with allure.step("Отображается сообщение 'Your search returned no results'"):
        assert "Your search returned no results." in page.search_results_message()


@allure.title("PL-11 Поиск товара по полному названию")
def test_search_for_full_product_name(browser):
    page = Search(browser)
    page.open(URL.BASE_URL)
    page.send_search_field("Ina Compression Short")
    page.send_enter()
    with allure.step("Товар присутствует в результатах поиска"):
        assert page.find_elem_by_name_in_results(name="Ina Compression Short"), "Название товара в списке не найдено"
