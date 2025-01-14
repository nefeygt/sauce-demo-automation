def pytest_bdd_before_scenario(request, feature, scenario):
    """Called before scenario is executed."""
    pass

def pytest_bdd_after_scenario(request, feature, scenario):
    """Called after scenario is executed."""
    context = request.getfixturevalue("context")
    if hasattr(context, "driver"):
        context.driver.quit()