from pages.main_page import MainPage
from data.urls import URL


def test_logo_is_loaded(browser):
    page = MainPage(browser)
    page.open(URL.BASE_URL)
    assert page.logo_is_visible(), "Лого отсутствует"


def test_search_box_is_loaded(browser):
    page = MainPage(browser)
    page.open(URL.BASE_URL)
    page.search_box_is_visible()
    page.search_box_button_is_visible()
    assert page.search_box_placeholder() == "Search entire store here..."
