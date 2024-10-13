import allure

from base.base_page import BasePage
from locators.item_locators import ItemLocators


class MiniItem(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Выбор элемента без опций и добавление его в корзину")
    def choose_item_and_add_to_cart(self, num_item: int = 0):
        elems = self.all_elems_is_visibles(ItemLocators.MINI_ITEMS)
        self.hold_mouse_on_element(elems[num_item])
        return self.is_clickable(ItemLocators.MINI_ITEMS_ADD_TO_CART).click()

    @allure.step("Выбор элемента и добавление его в список желаний")
    def choose_item_and_add_to_wish_list(self, num_item: int = 0):
        elems = self.all_elems_is_visibles(ItemLocators.MINI_ITEMS)
        self.hold_mouse_on_element(elems[num_item])
        return self.is_clickable(ItemLocators.MINI_ITEMS_ADD_TO_WISH_LIST).click()

    @allure.step("Выбор оранжевого цвета")
    def choose_items_color_orange(self, num_item: int = 0):
        elems = self.all_elems_is_visibles(ItemLocators.MINI_ITEMS_COLOR_ORANGE)
        return elems[num_item].click()

    @allure.step("Получение сообщение на странице товара")
    def get_message_item_page(self):
        return self.get_text(ItemLocators.MESSAGE_ITEMS_PAGE)

    @allure.step("Получение сообщение на странице авторизации")
    def get_message_login_page(self):
        return self.get_text(ItemLocators.MESSAGE_LOGIN_PAGE)

    @allure.step("Выбор цвета и размера товара")
    def item_options(self):
        pass
