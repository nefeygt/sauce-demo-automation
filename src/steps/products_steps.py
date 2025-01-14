from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config import TestConfig
import time

@given('I am logged in as a standard user')
def step_impl(context):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Initialize WebDriver
    context.driver = webdriver.Chrome(options=chrome_options)
    
    # Login
    login_page = LoginPage(context.driver)
    login_page.navigate()
    login_page.login(
        TestConfig.TEST_USERS["standard"]["username"],
        TestConfig.TEST_USERS["standard"]["password"]
    )
    
    # Initialize products page
    context.products_page = ProductsPage(context.driver)
    # Wait for products page to load
    assert context.products_page.is_on_products_page(), "Products page did not load"

@given('I add "{product_name}" to the cart')
@when('I add "{product_name}" to the cart')
def step_impl(context, product_name):
    context.products_page.add_product_to_cart(product_name)
    time.sleep(1)  # Wait for cart to update

@when('I sort products by "{sort_option}"')
def step_impl(context, sort_option):
    context.products_page.sort_products(sort_option)
    time.sleep(1)  # Wait for sorting to complete

@then('products should be sorted by price in ascending order')
def step_impl(context):
    time.sleep(1)  # Wait for sorting to complete
    prices = context.products_page.get_product_prices()
    assert prices == sorted(prices), "Products are not sorted in ascending order"

@then('products should be sorted by price in descending order')
def step_impl(context):
    time.sleep(1)  # Wait for sorting to complete
    prices = context.products_page.get_product_prices()
    assert prices == sorted(prices, reverse=True), "Products are not sorted in descending order"

@when('I remove "{product_name}" from the cart')
def step_impl(context, product_name):
    context.products_page.remove_product_from_cart(product_name)
    time.sleep(1)  # Wait for cart to update

@then('the cart count should be "{count}"')
def step_impl(context, count):
    actual_count = context.products_page.get_cart_count()
    assert str(actual_count) == count, f"Cart count is {actual_count}, expected {count}"

@then('the "{product_name}" should show "{button_text}" button')
def step_impl(context, product_name, button_text):
    actual_text = context.products_page.get_button_text(product_name)
    assert button_text.lower() in actual_text.lower(), \
        f"Button shows '{actual_text}', expected text containing '{button_text}'"