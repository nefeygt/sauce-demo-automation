from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config import TestConfig
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=chrome_options)

@given('I am logged in as a standard user')
def step_impl(context):
    context.driver = setup_driver()
    login_page = LoginPage(context.driver)
    login_page.navigate()
    time.sleep(1)  # Wait for page load
    
    # Login with standard user
    login_page.login(
        TestConfig.TEST_USERS["standard"]["username"],
        TestConfig.TEST_USERS["standard"]["password"]
    )
    time.sleep(1)  # Wait for login
    
    # Initialize and verify products page
    context.products_page = ProductsPage(context.driver)
    assert context.products_page.is_on_products_page(), "Failed to reach products page"

@when('I sort products by "{sort_option}"')
def step_impl(context, sort_option):
    context.products_page.sort_products(sort_option)
    time.sleep(2)  # Wait for sorting to complete

@then('products should be sorted by price in ascending order')
def step_impl(context):
    time.sleep(1)
    prices = context.products_page.get_product_prices()
    sorted_prices = sorted(prices)
    assert prices == sorted_prices, f"Products not sorted correctly. Current: {prices}, Expected: {sorted_prices}"

@then('products should be sorted by price in descending order')
def step_impl(context):
    time.sleep(1)
    prices = context.products_page.get_product_prices()
    sorted_prices = sorted(prices, reverse=True)
    assert prices == sorted_prices, f"Products not sorted correctly. Current: {prices}, Expected: {sorted_prices}"

@when('I add "{product_name}" to the cart')
def step_impl(context, product_name):
    context.products_page.add_product_to_cart(product_name)
    time.sleep(1)

@when('I remove "{product_name}" from the cart')
def step_impl(context, product_name):
    context.products_page.remove_product_from_cart(product_name)
    time.sleep(1)

@then('the cart count should be "{count}"')
def step_impl(context, count):
    time.sleep(1)
    actual_count = context.products_page.get_cart_count()
    assert str(actual_count) == count, f"Cart count is {actual_count}, expected {count}"

@then('the "{product_name}" should show "{button_text}" button')
def step_impl(context, product_name, button_text):
    time.sleep(1)
    actual_text = context.products_page.get_button_text(product_name)
    assert button_text.lower() in actual_text.lower(), \
        f"Button shows '{actual_text}', expected text containing '{button_text}'"