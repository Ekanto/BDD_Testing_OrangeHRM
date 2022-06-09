Feature: OrangeHRM Login
  Scenario: Checking the log in of OrangeHRM
    Given Launch the Firefox browser
    When Open OrangeHRM log in page
    And Putting the username "admin"
    And Putting the password "admin123"
    Then Verify the successfull log in attempt
    When Close the browser

  Scenario Outline: Checking the log in of OrangeHRM using multiple parameters
    Given Launch the Firefox browser
    When Open OrangeHRM log in page
    And Putting the username "<username>"
    And Putting the password "<password>"
    Then Verify the successfull log in attempt
    When Close the browser

    Examples:
      | username  | password |
      | admin     | admin123 |
      | admin 123 | admin123 |
      | admi      | admin123 |
      | 928374    | admin123 |
      | Admin     | admin123 |
