class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url: str):
        return self.browser.get(url)

    