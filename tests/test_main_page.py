from pages.main_page import MainPage
from data.urls import URL


def test_logo_is_loaded(browser):
    page = MainPage(browser)
    page.open(URL.BASE_URL)
    page.find_logo()
