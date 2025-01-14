from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    def navigate(self):
        """Navigate to login page"""
        self.logger.info(f"Navigating to {self.url}")
        self.driver.get(self.url)
        self.logger.info("Successfully loaded login page")

    def login(self, username, password):
        """Perform login with given credentials"""
        self.logger.info(f"Attempting login with username: {username}")
        self.input_text(*self.USERNAME_INPUT, username)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)
        self.logger.info("Login attempt completed")

    def get_error_message(self):
        """Get error message text if present"""
        error_message = self.get_text(*self.ERROR_MESSAGE)
        self.logger.info(f"Error message displayed: {error_message}")
        return error_message

    def is_on_login_page(self):
        """Verify if we're on login page"""
        return self.is_element_visible(*self.LOGIN_BUTTON)