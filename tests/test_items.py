import time

import allure
import pytest
from pages.item_page import MiniItem
from data.urls import URL


@allure.suite("Товары")
class TestMiniItems:
    @allure.title("PL-17 Добавить товар(одежда) в корзину не открывая страницу товара и не выбирая опции(цвет, размер)")
    def test_add_to_cart_without_option(self, browser):
        page = MiniItem(browser)
        page.open(URL.BASE_URL)
        page.choose_item_and_add_to_cart(num_item=3)
        time.sleep(30)
        with allure.step("Ошибка добовления товара в карзину"):
            assert page.get_message_item_page() == "You need to choose options for your item."

    @allure.title("")
    def test_add_to_catr_without_size(self, browser):
        page = MiniItem(browser)
        page.open(URL.BASE_URL)
        page.choose_items_color_orange()
        page.choose_item_and_add_to_cart()
        with allure.step("Ошибка добовления товара в карзину"):
            assert page.get_message_item_page() == "You need to choose options for your item."

    @allure.title("")
    def test_add_to_wishlist(self, browser):
        page = MiniItem(browser)
        page.open(URL.BASE_URL)
        page.choose_item_and_add_to_wish_list()
        with allure.step("Ошибка добовления товара в wishlist"):
            assert page.get_message_login_page() == "You must login or register to add items to your wishlist."

    @allure.title("")
    @pytest.mark.usefixtures("sing_in")
    def test_add_wishlist_sing_in(self, browser):
        page = MiniItem(browser)
        page.open(URL.BASE_URL)
        page.choose_item_and_add_to_wish_list()
        with allure.step("Товар успешно добавлет в wishlist"):
            assert page.get_message_item_page() == "Radiant Tee has been added to your Wish List. Click here to continue shopping."

