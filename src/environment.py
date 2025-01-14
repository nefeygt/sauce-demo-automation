from behave.model_core import Status
import allure
from selenium.webdriver.remote.webdriver import WebDriver

def before_all(context):
    pass

def after_step(context, step):
    if hasattr(context, 'driver'):
        # Capture screenshot if step failed
        if step.status == Status.failed:
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        # Capture screenshot after each scenario
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
        context.driver.quit()
        # Clean up after each scenario
        if hasattr(context, 'driver'):
            context.driver.quit()