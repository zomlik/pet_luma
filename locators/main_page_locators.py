from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.CSS_SELECTOR, ".logo")
    SEARCH_BOX = (By.CSS_SELECTOR, "#search")
    SEARCH_BOX_BUTTON = (By.CSS_SELECTOR, ".action.search")
