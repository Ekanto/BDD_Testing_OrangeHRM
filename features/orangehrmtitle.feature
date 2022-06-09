Feature: OrangeHRM Logo

  Scenario: Presense of the logo on OrangeHRM Page
    Given Launch Firefox browser
    When Open Orange hrm homepage
    Then Verify that the logo exists on the page
    And close the browser