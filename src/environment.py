import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def before_all(context):
    # Create reports directory if it doesn't exist
    if not os.path.exists("reports"):
        os.makedirs("reports")

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        try:
            context.driver.quit()
        except:
            pass

def after_step(context, step):
    if step.status == "failed" and hasattr(context, 'driver'):
        # Take screenshot on failure
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        screenshot_path = f"reports/screenshot-{timestamp}.png"
        try:
            context.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
        except:
            print("Failed to take screenshot")