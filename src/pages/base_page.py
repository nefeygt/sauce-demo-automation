from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def find_elements(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def input_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def is_element_visible(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except:
            return False

    def get_text(self, by, value):
        element = self.find_element(by, value)
        return element.text