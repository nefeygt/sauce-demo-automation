from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from config import Locators

class ProductsPage(BasePage):
    def is_on_products_page(self):
        """Verify if we're on products page"""
        return self.is_element_visible(*Locators.PRODUCT_TITLE)
    
    def sort_products(self, sort_option):
        """Sort products by given option"""
        dropdown = self.wait.until(
            EC.element_to_be_clickable(Locators.SORT_DROPDOWN)
        )
        select = Select(dropdown)
        select.select_by_visible_text(sort_option)
    
    def get_product_prices(self):
        """Get list of product prices"""
        try:
            # Wait for prices to be visible
            self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
            )
            prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
            return [float(price.text.replace("$", "")) for price in prices]
        except Exception as e:
            print(f"Error getting product prices: {str(e)}")
            return []
    
    def add_product_to_cart(self, product_name):
        """Add a product to cart by its name"""
        button = self._get_add_to_cart_button(product_name)
        button.click()
    
    def remove_product_from_cart(self, product_name):
        """Remove a product from cart by its name"""
        button = self._get_remove_button(product_name)
        button.click()
    
    def get_cart_count(self):
        """Get number of items in cart"""
        try:
            badge = self.find_element(*Locators.CART_BADGE)
            return int(badge.text)
        except:
            return 0
    
    def get_button_text(self, product_name):
        """Get the button text (Add to cart/Remove) for a product"""
        container = self._get_product_container(product_name)
        button = container.find_element(By.CSS_SELECTOR, "button")
        return button.text
    
    def _get_product_container(self, product_name):
        """Get product container element by product name"""
        return self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, 
                f"//div[contains(@class, 'inventory_item')]//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]"
            ))
        )
    
    def _get_add_to_cart_button(self, product_name):
        """Get add to cart button for a product"""
        container = self._get_product_container(product_name)
        return self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[id^='add-to-cart']")
            )
        )
    
    def _get_remove_button(self, product_name):
        """Get remove button for a product"""
        container = self._get_product_container(product_name)
        return container.find_element(By.CSS_SELECTOR, "button[id^='remove']")