from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import platform

def before_scenario(context, scenario):
    """Initialize WebDriver before each scenario"""
    # Set up Chrome options
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
        # In CI environment, ChromeDriver is started separately
        context.driver = webdriver.Chrome(options=chrome_options)
    else:
        # Local environment with manual ChromeDriver
        chromedriver_path = 'chromedriver.exe' if platform.system() == 'Windows' else 'chromedriver'
        service = Service(chromedriver_path)
        context.driver = webdriver.Chrome(service=service, options=chrome_options)
    
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    """Clean up after each scenario"""
    if hasattr(context, 'driver'):
        context.driver.quit()