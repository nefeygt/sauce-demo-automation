def before_all(context):
    # You can add any setup that needs to happen before all tests
    pass

def after_all(context):
    # Cleanup after all tests
    pass

def after_scenario(context, scenario):
    # Cleanup after each scenario
    if hasattr(context, 'driver'):
        context.driver.quit()