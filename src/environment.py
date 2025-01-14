def before_all(context):
    pass

def after_all(context):
    pass

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()