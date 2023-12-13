from selenium.webdriver.common.by import By


class ItemLocators:
    MINI_ITEMS = (By.CSS_SELECTOR, ".product-item")
    MINI_ITEMS_NAME = (By.CSS_SELECTOR, ".product.name.product-item-name")
