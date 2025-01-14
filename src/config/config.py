import os
from selenium.webdriver.common.by import By

class TestConfig:
    # Base URL
    BASE_URL = "https://www.saucedemo.com"
    
    # Timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30
    
    # Test Users
    TEST_USERS = {
        "standard": {
            "username": "standard_user",
            "password": "secret_sauce"
        },
        "locked": {
            "username": "locked_out_user",
            "password": "secret_sauce"
        },
        "problem": {
            "username": "problem_user",
            "password": "secret_sauce"
        }
    }
    
    # Browser Settings
    BROWSER_OPTIONS = {
        "headless": False,  # Set to True for headless mode
        "window_size": {"width": 1920, "height": 1080},
        "screenshots_on_failure": True
    }
    
    # Directory Paths
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    REPORTS_DIR = os.path.join(ROOT_DIR, "..", "reports")
    SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
    LOGS_DIR = os.path.join(ROOT_DIR, "..", "logs")

    # Create required directories if they don't exist
    @classmethod
    def create_directories(cls):
        for directory in [cls.REPORTS_DIR, cls.SCREENSHOTS_DIR, cls.LOGS_DIR]:
            if not os.path.exists(directory):
                os.makedirs(directory)

class Locators:
    """
    Central place to store all locators
    """
    # Login Page
    LOGIN_USERNAME = (By.ID, "user-name")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGIN_ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    
    # Products Page
    PRODUCT_TITLE = (By.CLASS_NAME, "title")
    PRODUCTS_LIST = (By.CLASS_NAME, "inventory_item")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    # Product Item
    ADD_TO_CART_BUTTON = lambda product_id: (
        By.CSS_SELECTOR, 
        f"[data-test='add-to-cart-{product_id}']"
    )
    REMOVE_BUTTON = lambda product_id: (
        By.CSS_SELECTOR, 
        f"[data-test='remove-{product_id}']"
    )