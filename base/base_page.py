import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    """ Базовый класс для страниц веб-приложения, использующий Selenium для взаимодействия
     с элементами на странице.
     Metods:
        open(): Открывает URL страницы в браузере
    """
    TIMEOUT = 15

    def __init__(self, browser):
        self.browser = browser

    def current_url(self):
        return self.browser.current_url

    @allure.step("Открытие траницы")
    def open(self, url: str):
        return self.browser.get(url)

    def get_text(self, locator: tuple) -> str:
        return self.is_visible(locator).text

    def len(self, locator: tuple) -> int:
        return len(self.all_elems_is_visibles(locator))

    def is_visible(self, locator: tuple, timeout: int = TIMEOUT) -> WebElement:
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator: tuple, timeout: int = TIMEOUT) -> WebElement:
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def all_elems_is_visibles(self, locator: tuple, timeout: int = TIMEOUT) -> list[WebElement]:
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def find(self, locator: tuple) -> WebElement:
        return self.browser.find_element(*locator)
