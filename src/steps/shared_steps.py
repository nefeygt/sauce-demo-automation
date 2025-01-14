from behave import given
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config import TestConfig
import time

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=chrome_options)

@given('I add "{product_name}" to the cart')
def step_impl(context, product_name):
    if not hasattr(context, 'products_page'):
        # If we don't have a products page, we need to log in first
        context.driver = create_driver()
        login_page = LoginPage(context.driver)
        login_page.navigate()
        login_page.login(
            TestConfig.TEST_USERS["standard"]["username"],
            TestConfig.TEST_USERS["standard"]["password"]
        )
        context.products_page = ProductsPage(context.driver)
        time.sleep(1)  # Wait for products page to load
    
    context.products_page.add_product_to_cart(product_name)
    time.sleep(1)  # Wait for cart update