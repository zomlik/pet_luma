from selenium.webdriver.common.by import By


class CreateAccountLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#lastname")
    EMAIL = (By.CSS_SELECTOR, "#email_address")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#password-confirmation")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".action.submit.primary")

    FIRST_NAME_ERROR = (By.CSS_SELECTOR, "#firstname-error")
    LAST_NAME_ERROR = (By.CSS_SELECTOR, "#lastname-error")
    EMAIL_ERROR = (By.CSS_SELECTOR, "#email_address-error")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "#password-error")
    CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, "#password-confirmation-error")

    MESSAGE = (By.CSS_SELECTOR, ".messages")
