from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage(BasePage):
    # Locators
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        super().__init__(driver)

    def is_on_products_page(self):
        """Verify if we're on products page"""
        return self.is_element_visible(*self.PRODUCTS_TITLE)