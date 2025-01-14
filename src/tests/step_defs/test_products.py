from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# Import all scenarios from our feature file
scenarios('../features/products.feature')

@given(parsers.parse('I am logged in as "{username}"'))
def login_user(driver, username):
    driver.get("https://www.saucedemo.com")
    login_page = LoginPage(driver)
    login_page.login(username, "secret_sauce")

@given('I am on the products page')
def verify_products_page(driver):
    products_page = ProductsPage(driver)
    assert products_page.is_current_page()

@when(parsers.parse('I select sorting option "{option}"'))
def select_sort_option(driver, option):
    products_page = ProductsPage(driver)
    products_page.select_sort_option(option)

@then('products should be sorted by price in ascending order')
def verify_price_ascending(driver):
    products_page = ProductsPage(driver)
    prices = products_page.get_product_prices()
    assert prices == sorted(prices)

@then('products should be sorted by price in descending order')
def verify_price_descending(driver):
    products_page = ProductsPage(driver)
    prices = products_page.get_product_prices()
    assert prices == sorted(prices, reverse=True)