from selenium.webdriver.common.by import By


class LoginPageLocator:
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#pass")
    SING_IN_BUTTON = (By.CSS_SELECTOR, ".action.login.primary")
