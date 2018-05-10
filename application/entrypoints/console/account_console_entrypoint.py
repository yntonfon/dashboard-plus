import argparse

from application.configuration import config
from application.configuration.ioc_database import IOCDatabase
from application.configuration.ioc_usecase import IOCUsecaseSteps
from application.core.exception.dashboardplus_exception import (
    InputValidationException, AccountAlreadyExistsException,
    AppUnexpectedFailureException
)


def main(user_inputs):
    create_account_use_case = IOCUsecaseSteps.create_account_step()
    credentials = user_inputs or ask_for_credentials()

    try:
        account_id = create_account_use_case.execute(credentials)
    except InputValidationException as error:
        print('Failed to create your account, due to invalid data -> ', error.messages)
    except AccountAlreadyExistsException as error:
        print('Failed to create your account, due to an existing one -> ', error.messages)
    except AppUnexpectedFailureException as error:
        print('An error occured while processing your request', error)
    else:
        print('Your account has been succesfully created with id ', account_id)


def ask_for_credentials():
    username = input('Choose a username: ')
    email = input('Choose an email: ')
    password = input('Choose a strong password: ')
    print('\n')

    return {
        'username': username,
        'email': email,
        'password': password
    }


def print_welcome_message():
    print('Welcome to Dashboard Plus interface')
    print('First step would be to create an account')
    print('\n')


def init_app():
    app_config = config()
    IOCDatabase.db().init_db(app_config['DATABASE_URL'], app_config['DATABASE_LOGGER_ACTIVE'])


def get_user_inputs():
    user_inputs = {}
    parser = define_arg_parser()
    args = parser.parse_args()

    if args.username:
        user_inputs['username'] = args.username
    if args.email:
        user_inputs['email'] = args.email
    if args.password:
        user_inputs['password'] = args.password

    return user_inputs


def define_arg_parser():
    parser = argparse.ArgumentParser(description='Manage account.')
    parser.add_argument("create", help="create a new account")
    parser.add_argument("--username", help="username for the account")
    parser.add_argument("--email", help="email for the account")
    parser.add_argument("--password", help="password for the account")
    return parser


if __name__ == "__main__":
    init_app()
    print_welcome_message()
    inputs = get_user_inputs()
    main(inputs)
    exit(0)
