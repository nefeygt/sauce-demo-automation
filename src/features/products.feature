Feature: Product Page Functionality
    As a customer of Sauce Demo
    I want to be able to sort products and add them to cart
    So that I can easily find and purchase items

    Background:
        Given I am logged in as a standard user

    Scenario: Sort products by price low to high
        When I sort products by "Price (low to high)"
        Then products should be sorted by price in ascending order

    Scenario: Sort products by price high to low
        When I sort products by "Price (high to low)"
        Then products should be sorted by price in descending order

    Scenario: Add multiple items to cart
        When I add "Sauce Labs Backpack" to the cart
        And I add "Sauce Labs Bike Light" to the cart
        Then the cart count should be "2"
        And the "Sauce Labs Backpack" should show "Remove" button
        And the "Sauce Labs Bike Light" should show "Remove" button

    Scenario: Remove item from cart
        Given I am logged in as a standard user
        And I add "Sauce Labs Backpack" to the cart
        When I remove "Sauce Labs Backpack" from the cart
        Then the cart count should be "0"
        And the "Sauce Labs Backpack" should show "Add to cart" button