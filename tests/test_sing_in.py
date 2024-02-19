import allure
from pages.sing_in import SingIn
from data.urls import URL
from data.fake_data import FakeData
from data.test_data import TestsData


@allure.suite("Авторизация")
class TestSingIn(FakeData):
    @allure.title("Переход на страницу регистации по кнопле Create an Account")
    def test_click_cteate_account_button(self, browser):
        page = SingIn(browser)
        page.open(URL.LOGIN_PAGE)
        page.click_create_account_button()
        with allure.step("Страница регистрации"):
            assert page.current_url() == URL.CREATE_ACCOUNT

    @allure.title("Переход на страницу Forgot Password")
    def test_click_forgot_password_link(self, browser):
        page = SingIn(browser)
        page.open(URL.LOGIN_PAGE)
        page.click_forgot_password_link()
        with allure.step("Страница Forgot Password"):
            assert page.current_url() == URL.FORGOT_PASSWORD

    @allure.title("Базавая Авторизация")
    def test_sing_in(self, browser):
        page = SingIn(browser)
        page.open(URL.LOGIN_PAGE)
        page.send_email(TestsData.EMAIL)
        page.send_password(TestsData.PASSWORD)
        page.click_sing_in_button()
        with allure.step("Сообщение об успешной авторизации"):
            assert "Welcome" in page.welcome_message()

    @allure.title("Авторизация с пустым полем Email")
    def test_empty_email_field(self, browser):
        page = SingIn(browser)
        page.open(URL.LOGIN_PAGE)
        page.send_password("1236594596")
        page.click_sing_in_button()
        with allure.step("Ошибка This is a required field"):
            assert page.email_errors_messages() == "This is a required field."

    @allure.title("Авторизация с пустым полем Password")
    def test_empty_password_field(self, browser):
        page = SingIn(browser)
        page.open(URL.LOGIN_PAGE)
        page.send_email(self.email())
        page.click_sing_in_button()
        with allure.step("Ошибка This is a required field"):
            assert page.pass_errors_messages() == "This is a required field."

