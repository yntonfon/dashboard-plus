Feature: Create a new account

  Scenario: Successfully creating an account
    Given a username blackops, an email blackops@gmail.com and a password Mystique_Secret
    When I ask to create my account
    Then my account should be created
    And my identifier should be 1
