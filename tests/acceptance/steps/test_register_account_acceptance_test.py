import pytest
from pytest_bdd import scenario, given, parsers, when, then

from application.core.usecase.usecase_input import UsecaseInput


@pytest.fixture()
def usecase_input():
    return ''


@pytest.mark.acceptance_test
@scenario('../register_account.feature', 'Successfully registering the new account')
def test_successfully_registering_account():
    pass


@given(parsers.parse('a username {username}, an email {email}, a password {password}'), target_fixture='usecase_input')
def account_data(username, email, password):
    return UsecaseInput(payload=dict(username=username, email=email, password=password))


@when('I ask to register a new account')
def register_account(usecase_input):
    print('register account with', usecase_input)


@then('my account should be created')
def account_is_created():
    print('account has been created')


@then(parsers.parse('I should receive an email at {email} with my activation account link'))
def activation_link_received(email):
    print('email with activation link send to', email)


@pytest.mark.acceptance_test
@scenario('../register_account.feature', 'Missing account data for registering the new account')
def test_missing_account_data_for_registering_account():
    pass


@given('no account data', target_fixture='usecase_input')
def no_account_data():
    return UsecaseInput()


@then('an error is returned with the corresponding missing data')
def missing_data_error():
    print('an error is returned')


@pytest.mark.acceptance_test
@scenario('../register_account.feature', 'Bad email for registering the new account')
def test_bad_email_for_registering_account():
    pass


@then('an error is returned with the corresponding bad data')
def bad_email_error():
    print('invalid email format')
