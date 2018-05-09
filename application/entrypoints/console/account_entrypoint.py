import argparse

from application.configuration.ioc_providers import IOCProviders
from application.core.exception.dashboardplus_exception import (
    AppDataValidationException, AppDataDuplicationException,
    AppUnexpectedFailureException
)
from application.core.factory.account_factory import AccountFactory
from application.core.usecase.create_new_account_use_case import CreateNewAccountUseCase
from application.providers.data import DatabaseAccessLayer
from application.providers.data.account_data_provider import AccountDataProvider


def main(inputs):
    create_account_use_case = prepare_use_case()
    print_welcome_message()
    credentials = inputs or ask_for_credentials()

    try:
        id = create_account_use_case.execute(credentials)
    except AppDataValidationException as error:
        print('Failed to create your account, due to invalid data -> ', error.messages)
    except AppDataDuplicationException as error:
        print('Failed to create your account, due to an existing one -> ', error.messages)
    except AppUnexpectedFailureException as error:
        print('An error occured while processing your request', error)
    else:
        print('Your account has been succesfully created with id ', id)


def prepare_use_case():
    account_validator_provider = IOCProviders.account_validator_provider()
    password_security_provider = IOCProviders.password_security_provider()
    factory = AccountFactory()
    db = DatabaseAccessLayer()
    db.init_db('', True)
    repository = AccountDataProvider(db)
    use_case = CreateNewAccountUseCase(account_validator_provider, password_security_provider, factory, repository)
    return use_case


def ask_for_credentials():
    username = input('Choose a username: ')
    email = input('Choose an email: ')
    password = input('Choose a strong password: ')
    return {
        'username': username,
        'email': email,
        'password': password
    }


def print_welcome_message():
    print('Welcome to Dashboard Plus interface')
    print('First step would be to create an account')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manage account.')
    parser.add_argument("create", help="create a new account")
    parser.add_argument("--username", help="username for the account")
    parser.add_argument("--email", help="email for the account")
    parser.add_argument("--password", help="password for the account")
    args = parser.parse_args()

    inputs = {}

    if args.username:
        inputs['username'] = args.username
    if args.email:
        inputs['email'] = args.email
    if args.password:
        inputs['password'] = args.password

    main(inputs)
