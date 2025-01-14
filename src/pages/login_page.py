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

    def login(self, username, password):
        """Login with the given credentials"""
        self.input_text(*self.USERNAME_INPUT, username)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click_element(*self.LOGIN_BUTTON)

    def get_error_message(self):
        """Get the error message text if present"""
        return self.get_text(*self.ERROR_MESSAGE)

    def is_error_message_displayed(self):
        """Check if error message is displayed"""
        return self.is_element_visible(*self.ERROR_MESSAGE)