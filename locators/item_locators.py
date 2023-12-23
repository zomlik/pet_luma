from selenium.webdriver.common.by import By


class ItemLocators:
    MESSAGE_LOGIN_PAGE = (By.CSS_SELECTOR, ".page.messages")
    MINI_ITEMS = (By.CSS_SELECTOR, ".product-item")
    MINI_ITEMS_NAME = (By.CSS_SELECTOR, ".product.name.product-item-name")
    MINI_ITEMS_ADD_TO_CART = (By.CSS_SELECTOR, ".action.tocart.primary")
    MESSAGE_ITEMS_PAGE = (By.CSS_SELECTOR, ".page.messages")
    MINI_ITEMS_ADD_TO_WISH_LIST = (By.CSS_SELECTOR, ".action.towishlist")
