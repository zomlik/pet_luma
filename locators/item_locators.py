from selenium.webdriver.common.by import By


class ItemLocators:
    MESSAGE_LOGIN_PAGE = (By.CSS_SELECTOR, ".page.messages")
    MINI_ITEMS = (By.CSS_SELECTOR, ".product-item")
    MINI_ITEMS_NAME = (By.CSS_SELECTOR, ".product.name.product-item-name")
    MINI_ITEMS_ADD_TO_CART = (By.CSS_SELECTOR, ".action.tocart.primary")
    MESSAGE_ITEMS_PAGE = (By.CSS_SELECTOR, ".page.messages")
    MINI_ITEMS_ADD_TO_WISH_LIST = (By.CSS_SELECTOR, ".action.towishlist")
    MINI_ITEMS_COLOR_GREY = (By.CSS_SELECTOR, "option-label-color-93-item-52")
    MINI_ITEMS_COLOR_ORANGE = (By.XPATH, "//div[@option-label='Orange']")
