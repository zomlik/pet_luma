import allure
import pytest

from data.urls import URL
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@allure.suite("Главная страница")
class TestMainPage:
    @allure.title("Лого отображается на странице")
    def test_logo_is_loaded(self, browser):
        page = MainPage(browser)
        page.open(URL.BASE_URL)
        page.logo_is_visible()

    @allure.title("Строка поиска отображается на странице")
    def test_search_box_is_loaded(self, browser):
        page = MainPage(browser)
        page.open(URL.BASE_URL)
        page.search_box_is_visible()
        page.search_box_button_is_visible()
        assert page.search_box_placeholder() == "Search entire store here..."

    @allure.title("Баннеры отображаются на странице")
    @pytest.mark.parametrize("banner_locator", MainPageLocators.LIST_OF_BANNERS)
    def test_promo_banners(self, browser, banner_locator):
        page = MainPage(browser)
        page.open(URL.BASE_URL)
        with allure.step("Баннер отображается на странице"):
            page.is_visible(banner_locator)

    @allure.step("На странице присутствуют часто покупаемые товары")
    def test_hot_seller(self, browser):
        page = MainPage(browser)
        page.open(URL.BASE_URL)
        with allure.step("Проверка количества товаров на странице"):
            assert page.len(MainPageLocators.HOT_SELLER_ITEM) == 6
        with allure.step("Проверка заголовка"):
            assert page.get_text(MainPageLocators.HOT_SELLER_TEXT) == "Hot Sellers"

    @allure.title("Корзина")
    def test_cart_is_present(self, browser):
        page = MainPage(browser)
        page.open(URL.BASE_URL)
        page.click_cart()
        with allure.step("Нажатие на пустую корзину"):
            assert page.cart_empty_message() == "You have no items in your shopping cart."
