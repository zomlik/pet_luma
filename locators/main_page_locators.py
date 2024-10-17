from selenium.webdriver.common.by import By


class MainPageLocators:
    """Main page locators"""
    LOGO = (By.CSS_SELECTOR, ".logo")
    SEARCH_BOX = (By.CSS_SELECTOR, "#search")
    SEARCH_BOX_BUTTON = (By.CSS_SELECTOR, ".action.search")
    CART_ICON = (By.CSS_SELECTOR, ".action.showcart")
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, ".subtitle.empty")
    SIGN_IN = ()

    """Main page banners locators"""
    BANNER_MAIN = (By.CSS_SELECTOR, ".block-promo.home-main")
    BANNER_PANTS = (By.CSS_SELECTOR, ".block-promo.home-pants")
    BANNER_T_SHIRTS = (By.CSS_SELECTOR, ".block-promo.home-t-shirts")
    BANNER_ERIN = (By.CSS_SELECTOR, ".block-promo.home-erin")
    BANNER_PERFORMANCE = (By.CSS_SELECTOR, ".block-promo.home-performance")
    BANNER_ECO = (By.CSS_SELECTOR, ".block-promo.home-eco")
    LIST_OF_BANNERS = [BANNER_MAIN, BANNER_PANTS, BANNER_T_SHIRTS,
                       BANNER_ERIN, BANNER_PERFORMANCE, BANNER_ECO]

    """Hot seller locators"""
    HOT_SELLER_TEXT = (By.CSS_SELECTOR, ".content-heading h2")
    HOT_SELLER_ITEM = (By.CSS_SELECTOR, ".product-item")
