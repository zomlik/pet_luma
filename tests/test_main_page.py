import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data.urls import URL


@allure.suite("Главная страница")
class TestMainPage:
    @allure.title("PL-12 Лого отображается на странице")
    def test_logo_is_loaded(self, browser):
        page = MainPage(browser)
        page.open(URL.BASE_URL)
        page.logo_is_visible()

    @allure.title("PL-5 Строка поиска отображается на странице")
    def test_search_box_is_loaded(self, browser):
        page = MainPage(browser)
        page.open(URL.BASE_URL)
        page.search_box_is_visible()
        page.search_box_button_is_visible()
        assert page.search_box_placeholder() == "Search entire store here..."

    @allure.title("PL-14 Баннеры отображаются на странице")
    @pytest.mark.parametrize("banner_locator", MainPageLocators.LIST_OF_BANNERS)
    def test_promo_banners(self, browser, banner_locator):
        page = MainPage(browser)
        page.open(URL.BASE_URL)
        with allure.step("Баннер отображается на странице"):
            page.is_visible(banner_locator)

    @allure.step("PL-15 На странице присутствуют часто покупаемые товары")
    def test_hot_sellar(self, browser):
        page = MainPage(browser)
        page.open(URL.BASE_URL)
        with allure.step("Проверка количества товаров на странице"):
            assert page.len(MainPageLocators.HOT_SELLAR_ITEM) == 6
        with allure.step("Проверка заголовка"):
            assert page.get_text(MainPageLocators.HOT_SELLAR_TEXT) == "Hot Sellers"
