Feature: Register a new account

  Scenario: Successfully registering the new account
    Given a username blackops, an email blackops@gmail.com, a password Mystique_Secret
    When I ask to register a new account
    Then my account should be created
    And I should receive an email at blackops@gmail.com with my activation account link


  Scenario: Missing account data for registering the new account
    Given no account data
    When I ask to register a new account
    Then an error is returned with the corresponding missing data


  Scenario: Bad email for registering the new account
    Given a username blackops, an email blackops@@gmail.com, a password mystiqueSecret
    When I ask to register a new account
    Then an error is returned with the corresponding bad data
