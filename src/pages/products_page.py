from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from config import Locators

class ProductsPage(BasePage):
    def is_on_products_page(self):
        return self.is_element_visible(*Locators.PRODUCT_TITLE)
    
    def sort_products(self, sort_option):
        select = Select(self.find_element(*Locators.SORT_DROPDOWN))
        select.select_by_visible_text(sort_option)
    
    def get_product_prices(self):
        """Get list of product prices"""
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(price.text.replace("$", "")) for price in prices]
    
    def add_product_to_cart(self, product_name):
        """Add a product to cart by its name"""
        product_id = self._get_product_id_by_name(product_name)
        self.click(*Locators.ADD_TO_CART_BUTTON(product_id))
    
    def remove_product_from_cart(self, product_name):
        """Remove a product from cart by its name"""
        product_id = self._get_product_id_by_name(product_name)
        self.click(*Locators.REMOVE_BUTTON(product_id))
    
    def get_cart_count(self):
        """Get number of items in cart"""
        try:
            badge = self.find_element(*Locators.CART_BADGE)
            return int(badge.text)
        except:
            return 0
    
    def get_button_text(self, product_name):
        """Get the button text (Add to cart/Remove) for a product"""
        product_container = self._get_product_container(product_name)
        button = product_container.find_element(By.CSS_SELECTOR, "button")
        return button.text
    
    def _get_product_id_by_name(self, product_name):
        """Get product ID from product name"""
        product = self._get_product_container(product_name)
        button = product.find_element(By.CSS_SELECTOR, "button")
        button_id = button.get_attribute("data-test")
        return button_id.replace("add-to-cart-", "")
    
    def _get_product_container(self, product_name):
        """Get product container element by product name"""
        return self.driver.find_element(
            By.XPATH, 
            f"//div[contains(@class, 'inventory_item')]//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]"
        )