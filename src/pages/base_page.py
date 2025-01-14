from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        """Wait for element to be visible and return it"""
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def click(self, by, value):
        """Wait for element to be clickable and click it"""
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def input_text(self, by, value, text):
        """Wait for element to be visible and input text"""
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        """Get text from element"""
        element = self.find_element(by, value)
        return element.text

    def is_element_visible(self, by, value, timeout=10):
        """Check if element is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False