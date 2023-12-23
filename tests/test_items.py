import allure
from pages.item_page import MiniItem
from data.urls import URL


@allure.suite("Товары")
class TestMiniItems:
    @allure.title("")
    def test_add_to_cart_without_option(self, browser):
        page = MiniItem(browser)
        page.open(URL.BASE_URL)
        page.choose_item_and_add_to_cart()
        with allure.step("ОР: Для добовления товара в корзину нужно выбрать цвет, размер"):
            assert page.get_message_item_page() == "You need to choose options for your item."

    @allure.title("")
    def test_add_to_wish_list(self, browser):
        page = MiniItem(browser)
        page.open(URL.BASE_URL)
        page.choose_item_and_add_to_wish_list()
        with allure.step("ОР: Чтобы добавить товар в wishlist нужно быть авторизаванным"):
            assert page.get_message_login_page() == "You must login or register to add items to your wishlist."

    def test_add_item_catr_with_options(self, browser):
        page = MiniItem(browser)
        page.open(URL.BASE_URL)
        page.