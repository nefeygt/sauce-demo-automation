from selenium.webdriver.common.by import By
from .base_page import BasePage
from config import Locators, TestConfig

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = TestConfig.BASE_URL

    def navigate(self):
        """Navigate to login page"""
        self.driver.get(self.url)

    def login(self, username, password):
        """Perform login with given credentials"""
        self.input_text(*Locators.LOGIN_USERNAME, username)
        self.input_text(*Locators.LOGIN_PASSWORD, password)
        self.click(*Locators.LOGIN_BUTTON)

    def get_error_message(self):
        """Get error message text if present"""
        return self.get_text(*Locators.LOGIN_ERROR)

    def is_on_login_page(self):
        """Verify if we're on login page"""
        return self.is_element_visible(*Locators.LOGIN_BUTTON)