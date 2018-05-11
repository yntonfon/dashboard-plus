import pytest
from pytest_bdd import scenario, given, parsers, when, then

from application.core.usecase.usecase_input import UseCaseInput


@pytest.mark.acceptance_test
@scenario('../activate_account.feature', 'Successfully activating an account')
def test_successfully_activating_an_account():
    pass


@given(parsers.parse('a token {token}'), target_fixture='usecase_input')
@given(parsers.parse('an invalid token {token}'), target_fixture='usecase_input')
def a_token(token):
    return UseCaseInput(payload=token)


@when('I ask to activate an account')
def activate_account(usecase_input):
    print('activate account with', usecase_input)


@then('the account should be activated')
def account_is_activated():
    print('account is actived')


@pytest.mark.acceptance_test
@scenario('../activate_account.feature', 'Invalid token for activating an account')
def test_invalid_token():
    pass


@then('the account should not be activated')
def account_is_not_activated():
    print('account is not actived')


@then('an error is returned')
def error_message():
    print('error message is returned')
