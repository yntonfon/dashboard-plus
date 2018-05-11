Feature: Activate an account

  Scenario: Successfully activating an account
    Given a token ImJhc3RhcmRAZ21haWwuY29tIg.DdYiFw.--gx3W0EO4yI355Q9EiTL1ndhok
    When I ask to activate an account
    Then the account should be activated

  Scenario: Invalid token for activating an account
    Given an invalid token blablabla
    When I ask to activate an account
    Then the account should not be activated
    And an error is returned
