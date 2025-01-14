Feature: Product Page Functionality
    As a user of Sauce Demo
    I want to interact with products on the inventory page
    So that I can find and purchase items easily

    Background:
        Given I am logged in as "standard_user"
        And I am on the products page

    Scenario: Sort products by price low to high
        When I select sorting option "Price (low to high)"
        Then products should be sorted by price in ascending order

    Scenario: Sort products by price high to low
        When I select sorting option "Price (high to low)"
        Then products should be sorted by price in descending order

    Scenario: Sort products by name A to Z
        When I select sorting option "Name (A to Z)"
        Then products should be sorted by name in ascending order
        
    Scenario: Sort products by name Z to A
        When I select sorting option "Name (Z to A)"
        Then products should be sorted by name in descending order

    Scenario: Add single item to cart
        When I add the item "Sauce Labs Backpack" to cart
        Then the shopping cart badge should show "1"
        And the item "Sauce Labs Backpack" should have "Remove" button

    Scenario: Remove item from cart
        Given I have added "Sauce Labs Backpack" to cart
        When I remove the item "Sauce Labs Backpack" from cart
        Then the shopping cart badge should not be visible
        And the item "Sauce Labs Backpack" should have "Add to cart" button