Feature: Login Functionality
    As a user of Sauce Demo
    I want to be able to login
    So that I can access the products page

    Scenario: Successful login with valid credentials
        Given I am on the login page
        When I login with "standard_user" and "secret_sauce"
        Then I should be redirected to the products page

    Scenario: Failed login with invalid credentials
        Given I am on the login page
        When I login with "invalid_user" and "invalid_password"
        Then I should see an error message