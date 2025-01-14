from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config import TestConfig
import time

@given('I am on the login page')
def step_impl(context):
    # Set up WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    context.driver = webdriver.Chrome(options=chrome_options)
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()
    time.sleep(1)  # Wait for page load

@when('I login with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)
    time.sleep(1)  # Wait for login process

@then('I should be redirected to the products page')
def step_impl(context):
    products_page = ProductsPage(context.driver)
    assert products_page.is_on_products_page(), "Not redirected to products page"

@then('I should see an error message')
def step_impl(context):
    error_message = context.login_page.get_error_message()
    assert error_message != "", "No error message displayed"