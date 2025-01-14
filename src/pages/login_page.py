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
        self.driver.get(self.url)

    def login(self, username, password):
        """Perform login with given credentials"""
        self.input_text(*self.USERNAME_INPUT, username)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        """Get error message text if present"""
        return self.get_text(*self.ERROR_MESSAGE)

    def is_on_login_page(self):
        """Verify if we're on login page"""
        return self.is_element_visible(*self.LOGIN_BUTTON)