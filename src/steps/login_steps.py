from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    
    # Create Chrome service with path to chromedriver
    service = Service('chromedriver.exe')  # Adjust this path if chromedriver is elsewhere
    
    # Initialize the driver with service and options
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.get("https://www.saucedemo.com")
    
    # Wait for the login form to be present
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-name")))

@when('I login with "{username}" and "{password}"')
def step_impl(context, username, password):
    username_field = context.driver.find_element(By.ID, "user-name")
    password_field = context.driver.find_element(By.ID, "password")
    login_button = context.driver.find_element(By.ID, "login-button")
    
    username_field.clear()
    username_field.send_keys(username)
    password_field.clear()
    password_field.send_keys(password)
    login_button.click()

@then('I should be redirected to the products page')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    inventory_container = wait.until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
    assert inventory_container.is_displayed()
    context.driver.quit()

@then('I should see an error message')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    error_message = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert error_message.is_displayed()
    context.driver.quit()