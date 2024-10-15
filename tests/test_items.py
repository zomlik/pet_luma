import time

import allure
import pytest

from data.urls import URL
from pages.item_page import MiniItem


@allure.suite("Products")
class TestMiniItems:
    @allure.title("Add an item to the cart without opening the product"
                  " page and without selecting options)")
    def test_add_to_cart_without_option(self, browser):
        page = MiniItem(browser)
        page.open(URL.MAIN_MAIGE)
        page.choose_item_and_add_to_cart(num_item=3)
        time.sleep(30)
        with allure.step("Error adding an item to the cart"):
            assert page.get_message_item_page() == "You need to choose options for your item."

    @allure.title("")
    def test_add_to_cart_without_size(self, browser):
        page = MiniItem(browser)
        page.open(URL.MAIN_MAIGE)
        page.choose_items_color_orange()
        page.choose_item_and_add_to_cart()
        with allure.step("Error adding an item to the cart"):
            assert page.get_message_item_page() == "You need to choose options for your item."

    @allure.title("")
    def test_add_to_wishlist(self, browser):
        page = MiniItem(browser)
        page.open(URL.MAIN_MAIGE)
        page.choose_item_and_add_to_wish_list()
        with allure.step("Authorization error"):
            assert page.get_message_login_page() == ("You must login or register"
                                                     " to add items to your wishlist.")

    @allure.title("Add an item to your wish list")
    @pytest.mark.usefixtures("sing_in")
    def test_add_wishlist_sing_in(self, browser):
        page = MiniItem(browser)
        page.open(URL.MAIN_MAIGE)
        page.choose_item_and_add_to_wish_list()
        with allure.step("The product has been successfully added to wish list"):
            assert page.get_message_item_page() == ("Radiant Tee has been added to your Wish List."
                                                    " Click here to continue shopping.")
