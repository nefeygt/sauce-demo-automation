from selenium.webdriver.common.by import By
from .base_page import BasePage
from config import Locators

class ProductsPage(BasePage):
    def is_on_products_page(self):
        """Verify if we're on products page"""
        return self.is_element_visible(*Locators.PRODUCT_TITLE)
    
    def get_products_count(self):
        """Get the number of products displayed"""
        return len(self.driver.find_elements(*Locators.PRODUCTS_LIST))
    
    def sort_products(self, sort_option):
        """Sort products by the given option"""
        self.select_by_visible_text(*Locators.SORT_DROPDOWN, sort_option)
    
    def add_product_to_cart(self, product_id):
        """Add a product to cart by its ID"""
        self.click(*Locators.ADD_TO_CART_BUTTON(product_id))
    
    def get_cart_count(self):
        """Get the number of items in cart"""
        try:
            return int(self.get_text(*Locators.CART_BADGE))
        except:
            return 0