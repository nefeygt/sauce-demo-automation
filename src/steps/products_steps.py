from behave import given, when, then
from pages.products_page import ProductsPage
from pages.login_page import LoginPage

@given('I am logged in as "{username}"')
def step_impl(context, username):
    login_page = LoginPage(context.driver)
    login_page.login(username, "secret_sauce")

@given('I am on the products page')
def step_impl(context):
    context.products_page = ProductsPage(context.driver)
    assert context.products_page.is_current_page()

@when('I select sorting option "{option}"')
def step_impl(context, option):
    context.products_page.select_sort_option(option)

@then('products should be sorted by price in ascending order')
def step_impl(context):
    prices = context.products_page.get_product_prices()
    assert prices == sorted(prices), f"Prices not in ascending order. Current order: {prices}"

@then('products should be sorted by price in descending order')
def step_impl(context):
    prices = context.products_page.get_product_prices()
    assert prices == sorted(prices, reverse=True), f"Prices not in descending order. Current order: {prices}"

@then('products should be sorted by name in ascending order')
def step_impl(context):
    names = context.products_page.get_product_names()
    assert names == sorted(names), f"Names not in ascending order. Current order: {names}"

@then('products should be sorted by name in descending order')
def step_impl(context):
    names = context.products_page.get_product_names()
    assert names == sorted(names, reverse=True), f"Names not in descending order. Current order: {names}"

@when('I add the item "{item_name}" to cart')
def step_impl(context, item_name):
    context.products_page.add_item_to_cart(item_name)

@given('I have added "{item_name}" to cart')
def step_impl(context, item_name):
    context.products_page.add_item_to_cart(item_name)

@when('I remove the item "{item_name}" from cart')
def step_impl(context, item_name):
    context.products_page.remove_item_from_cart(item_name)

@then('the shopping cart badge should show "{count}"')
def step_impl(context, count):
    actual_count = context.products_page.get_cart_badge_count()
    assert actual_count == int(count), f"Expected cart count: {count}, but got: {actual_count}"

@then('the shopping cart badge should not be visible')
def step_impl(context):
    assert not context.products_page.is_cart_badge_visible(), "Cart badge is visible when it should not be"

@then('the item "{item_name}" should have "{button_text}" button')
def step_impl(context, item_name, button_text):
    actual_text = context.products_page.get_item_button_text(item_name)
    assert button_text in actual_text, f"Expected button text to contain '{button_text}', but got '{actual_text}'"