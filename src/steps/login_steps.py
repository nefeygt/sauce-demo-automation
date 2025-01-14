from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@given('I am on the login page')
def step_impl(context):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    try:
        # Initialize WebDriver with options
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )
        context.login_page = LoginPage(context.driver)
        context.login_page.navigate()
    except Exception as e:
        print(f"Failed to initialize WebDriver: {str(e)}")
        raise

# Rest of the code remains the same...

@when('I login with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@then('I should be redirected to the products page')
def step_impl(context):
    products_page = ProductsPage(context.driver)
    assert products_page.is_on_products_page(), "Not redirected to products page"

@then('I should see an error message')
def step_impl(context):
    error_message = context.login_page.get_error_message()
    assert error_message != "", "No error message displayed"

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()