import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    """ Базовый класс для страниц веб-приложения, использующий Selenium для взаимодействия
     с элементами на странице.
     Args:
        driver: WebDriver, экземпляр Selenium WebDriver для управления браузером
     Metods:
        open(): Открывает URL страницы в браузере
        current_url(): Возвращает текущий URL страницы
        get_text():
        len(): Возвращает количество элементов в списке
        is_visible(): Ожидает видимость элемента, заданного локатором, в течение указанного времени.
            Возвращает WebElement, если элемент видим, или вызывает исключение TimeoutException, если
                     элемент не появилс
        is_clickable(): Ожидает, что элемент, заданный локатором, станет кликабельным в течение указанного
                        времени. Если элемент становится кликабельным, функция возвращает элемент, иначе
                        вызывает исключение TimeoutException.
        all_elems_is_visibles():
        send_enter():


    """
    TIMEOUT = 15

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Open page")
    def open(self, url: str) -> None:
        return self.browser.get(url)

    def current_url(self) -> None:
        return self.browser.current_url

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.is_visible(locator).text

    def len(self, locator: tuple[str, str]) -> int:
        return len(self.all_elems_is_visibles(locator))

    def is_visible(self, locator: tuple[str, str], timeout: int = TIMEOUT) -> WebElement:
        return Wait(self.browser, timeout).until(ec.visibility_of_element_located(locator),
                                                 message=f"Can't find element by {locator}")

    def is_clickable(self, locator: tuple[str, str], timeout: int = TIMEOUT) -> WebElement:
        return Wait(self.browser, timeout).until(ec.element_to_be_clickable(locator),
                                                 message=f"Can't find element by {locator}")

    def all_elems_is_visibles(self, locator: tuple[str, str],
                              timeout: int = TIMEOUT) -> list[WebElement]:
        return Wait(self.browser, timeout).until(ec.visibility_of_all_elements_located(locator),
                                                 message=f"Can't find elements by {locator}")

    def find(self, locator: tuple) -> WebElement:
        return self.browser.find_element(*locator)

    def hold_mouse_on_element(self, elem) -> None:
        if type(elem) is WebElement:
            return ActionChains(self.browser).move_to_element(elem).perform()
        else:
            return ActionChains(self.browser).move_to_element(self.is_visible(elem)).perform()

    @allure.step("Нажатие клавиши Enter")
    def send_enter(self) -> None:
        return ActionChains(self.browser).send_keys(Keys.ENTER).perform()
