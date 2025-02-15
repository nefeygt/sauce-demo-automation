from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .base_page import BasePage
import time

class ProductsPage(BasePage):
    # Locators
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    
    def __init__(self, driver):
        super().__init__(driver)

    def is_current_page(self):
        """Verify that we are on the products page"""
        try:
            return self.driver.find_element(*self.INVENTORY_CONTAINER).is_displayed()
        except NoSuchElementException:
            return False

    def select_sort_option(self, option_text):
        """Select sorting option from dropdown"""
        # Get initial state
        initial_names = [name.text for name in self.driver.find_elements(*self.PRODUCT_NAMES)]
        
        # Select the option
        sort_dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        sort_dropdown.select_by_visible_text(option_text)
        
        # Wait for sort to take effect by checking for name changes
        def check_sort_complete(driver):
            current_names = [name.text for name in driver.find_elements(*self.PRODUCT_NAMES)]
            return current_names != initial_names
        
        try:
            self.wait.until(check_sort_complete)
        except TimeoutException:
            # If timeout occurs, give a small delay and continue
            # (sometimes the sort is instant and names don't change)
            time.sleep(1)

    def get_product_names(self):
        """Get list of all product names in current order"""
        # Wait for products to be visible
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_NAMES))
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_prices(self):
        """Get list of all product prices in current order"""
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(element.text.replace('$', '')) for element in elements]

    def add_item_to_cart(self, item_name):
        """Add specific item to cart"""
        button = self.driver.find_element(
            By.XPATH, 
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button[contains(text(), 'Add to cart')]"
        )
        button.click()

    def remove_item_from_cart(self, item_name):
        """Remove specific item from cart"""
        button = self.driver.find_element(
            By.XPATH, 
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button[text()='Remove']"
        )
        button.click()

    def get_cart_badge_count(self):
        """Get the current cart count from badge"""
        try:
            badge = self.driver.find_element(*self.SHOPPING_CART_BADGE)
            return int(badge.text)
        except NoSuchElementException:
            return 0

    def is_cart_badge_visible(self):
        """Check if cart badge is visible"""
        try:
            self.driver.find_element(*self.SHOPPING_CART_BADGE)
            return True
        except NoSuchElementException:
            return False

    def get_item_button_text(self, item_name):
        """Get the button text (Add to cart/Remove) for a specific item"""
        button = self.driver.find_element(
            By.XPATH, 
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        )
        return button.text