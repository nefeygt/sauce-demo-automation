from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from config import Locators

class ProductsPage(BasePage):
    # Keep existing methods...

    def remove_product_from_cart(self, product_name):
        """Remove a product from cart by its name"""
        try:
            product_container = self._get_product_container(product_name)
            remove_button = product_container.find_element(By.CSS_SELECTOR, "button.btn_secondary")
            remove_button.click()
        except Exception as e:
            print(f"Error removing product {product_name}: {str(e)}")
            raise

    def _get_product_container(self, product_name):
        """Get product container element by product name"""
        try:
            container = self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH, 
                    f"//div[contains(@class, 'inventory_item')]//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]"
                ))
            )
            return container
        except Exception as e:
            print(f"Error finding product container for {product_name}: {str(e)}")
            raise

    def _get_product_id_by_name(self, product_name):
        """Get product ID from product name"""
        try:
            product = self._get_product_container(product_name)
            button = product.find_element(By.CSS_SELECTOR, "button")
            button_id = button.get_attribute("data-test")
            # Handle both add and remove button IDs
            return button_id.replace("add-to-cart-", "").replace("remove-", "")
        except Exception as e:
            print(f"Error getting product ID for {product_name}: {str(e)}")
            raise

    def get_button_text(self, product_name):
        """Get the button text (Add to cart/Remove) for a product"""
        try:
            product_container = self._get_product_container(product_name)
            button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button"))
            )
            return button.text
        except Exception as e:
            print(f"Error getting button text for {product_name}: {str(e)}")
            raise