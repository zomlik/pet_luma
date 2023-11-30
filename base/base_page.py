from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    """ Базовый класс для страниц веб-приложения, использующий Selenium для взаимодействия
     с элементами на странице.
    """
    TIMEOUT = 15

    def __init__(self, browser):
        self.browser = browser

    def current_url(self):
        return self.browser.current_url

    def open(self, url: str):
        return self.browser.get(url)

    def is_visible(self, locator: tuple, timeout: int = TIMEOUT):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator: tuple, timeout: int = TIMEOUT):
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def find(self, locator: tuple):
        return self.browser.find_element(*locator)
