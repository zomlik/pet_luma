import allure
import pytest

from data.urls import URL
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@allure.suite("Main Page")
class TestMainPage:
    @allure.title("Check logo on main page")
    def test_click_on_logo(self, browser):
        page = MainPage(browser)
        page.open(URL.MAIN_MAIGE)
        page.click_on_logo()
        with allure.step("Check opened url"):
           assert page.current_url() == URL.MAIN_MAIGE

    @allure.title("The search bar is displayed on the page")
    def test_search_box_is_loaded(self, browser):
        page = MainPage(browser)
        page.open(URL.MAIN_MAIGE)
        page.search_box_is_visible()
        page.search_box_button_is_visible()
        assert page.search_box_placeholder() == "Search entire store here..."

    @allure.title("Banners are displayed on the page")
    @pytest.mark.parametrize("banner_locator", MainPageLocators.LIST_OF_BANNERS)
    def test_promo_banners(self, browser, banner_locator):
        page = MainPage(browser)
        page.open(URL.MAIN_MAIGE)
        with allure.step(f"Banner {banner_locator} is displayed on the page"):
            page.is_visible(banner_locator)

    @allure.title("The page contains hot seller products")
    def test_hot_seller(self, browser):
        page = MainPage(browser)
        page.open(URL.MAIN_MAIGE)
        with allure.step("The products are present on the page"):
            assert page.len(MainPageLocators.HOT_SELLER_ITEM) == 6
        with allure.step("Header: Hot Sellers"):
            assert page.get_text(MainPageLocators.HOT_SELLER_TEXT) == "Hot Sellers"

    @allure.title("he page contains Cart")
    def test_cart_is_present(self, browser):
        page = MainPage(browser)
        page.open(URL.MAIN_MAIGE)
        page.click_cart()
        with allure.step("Cart is working"):
            assert page.cart_empty_message() == "You have no items in your shopping cart."
