import pytest
from pytest_bdd import scenario, given, parsers, when, then


@pytest.mark.acceptance_test
@scenario('../create_account.feature', 'Successfully creating an account')
def test_create_account():
    pass


@given(parsers.parse('a username {username}, an email {email} and a password {password}'))
def choose_credentials(username, email, password):
    return dict(username=username, email=email, password=password)


@when('I ask to create my account')
def create_account(choose_credentials):
    print('Executed the creation with', choose_credentials)


@then('my account should be created')
def account_is_created():
    print('Account is created')


@then(parsers.parse('my identifier should be {id}'))
def identifier_is_returned(id):
    print('my identifier', id)
