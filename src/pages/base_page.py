from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = driver.logger if hasattr(driver, 'logger') else None

    def find_element(self, by, value):
        """Wait for element to be visible and return it"""
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            self.logger.debug(f"Found element: {value}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {value}")
            raise

    def click(self, by, value):
        """Wait for element to be clickable and click it"""
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            self.logger.debug(f"Clicked element: {value}")
        except Exception as e:
            self.logger.error(f"Failed to click element {value}: {str(e)}")
            raise

    def input_text(self, by, value, text):
        """Wait for element to be visible and input text"""
        try:
            element = self.find_element(by, value)
            element.clear()
            element.send_keys(text)
            self.logger.debug(f"Input text in element {value}: {text}")
        except Exception as e:
            self.logger.error(f"Failed to input text in element {value}: {str(e)}")
            raise