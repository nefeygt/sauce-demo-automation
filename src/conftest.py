import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import platform

@pytest.fixture(scope="function")
def driver():
    """Create a WebDriver instance for each test"""
    chrome_options = Options()
    
    # Add CI-specific options
    if os.getenv('CI'):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    else:
        chrome_options.add_argument('--start-maximized')
    
    # Setup ChromeDriver based on environment
    if os.getenv('CI'):
        driver = webdriver.Chrome(options=chrome_options)
    else:
        chromedriver_path = 'chromedriver.exe' if platform.system() == 'Windows' else 'chromedriver'
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()