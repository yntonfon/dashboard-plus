from application.core.exception.dashboardplus_exception import (
    AppDataValidationException, AppDataDuplicationException,
    AppUnexpectedFailureException
)
from application.core.factory.account_factory import AccountFactory
from application.core.usecase.create_new_account_use_case import CreateNewAccountUseCase
from application.providers.data.account_database_provider import AccountDatabaseDataProvider
from application.providers.security.password_security_provider import PasswordSecurityProvider
from application.providers.validator.account_validator_provider import AccountValidatorProvider
from application.providers.validator.schema.account_schema import AccountSchema


def main():
    print_welcome_message()
    credentials = ask_for_credentials()
    create_account_use_case = prepare_use_case()

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
    schema = AccountSchema()
    validator = AccountValidatorProvider(schema)
    encryptor = PasswordSecurityProvider()
    factory = AccountFactory()
    repository = AccountDatabaseDataProvider()
    use_case = CreateNewAccountUseCase(validator, encryptor, factory, repository)
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
    main()
