from utils.logger import Logger
import time

def before_all(context):
    context.logger = Logger()
    context.logger.info("Starting test execution")

def before_scenario(context, scenario):
    context.logger.info(f"Starting scenario: {scenario.name}")
    context.start_time = time.time()

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        if scenario.status == "failed":
            # Take screenshot on failure
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"screenshots/failed_scenario_{timestamp}.png"
            try:
                context.driver.save_screenshot(screenshot_path)
                context.logger.info(f"Screenshot saved: {screenshot_path}")
            except Exception as e:
                context.logger.error(f"Failed to take screenshot: {str(e)}")
        
        context.driver.quit()
    
    duration = time.time() - context.start_time
    context.logger.info(f"Scenario completed: {scenario.name} - Status: {scenario.status}")
    context.logger.info(f"Duration: {duration:.2f} seconds")

def after_step(context, step):
    if step.status == "failed":
        context.logger.error(f"Step failed: {step.name}")
        context.logger.error(f"Error message: {step.error_message}")