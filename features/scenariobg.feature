Feature: OrangeHRM Login

    Background: Common steps
        Given I launch the browser
        When I open application
        And Enter valid username and password
        And Click on login

    Scenario: Login to HRM application

        Then User must login to the dashboard page

    Scenario: Search user

        When Navigate to search page
        Then Search page should display

    Scenario: Advanced user search

        When Navigate to the advanced search page
        Then Advanced search page should display