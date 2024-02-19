from selenium.webdriver.common.by import By


class SingInLocators:
    EMAIL = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#pass")
    SING_IN_BUTTON = (By.CSS_SELECTOR, ".action.login.primary")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".action.create.primary")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, ".action.remind")

    EMAIL_ERROR = (By.CSS_SELECTOR, "#email-error")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "#pass-error")

    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".logged-in")
