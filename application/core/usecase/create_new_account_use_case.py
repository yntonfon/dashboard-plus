from application.core.entity.account import Account
from application.core.exception.dashboardplus_exception import (
    AppDataValidationException,
    EntityAlreadyExistsException,
    AppDataDuplicationException, PersitenceException,
    AppUnexpectedFailureException
)


class CreateNewAccountUseCase:
    def __init__(self, validator, encryptor, factory, repository):
        self.repository = repository
        self.factory = factory
        self.encryptor = encryptor
        self.validator = validator

    def execute(self, payload):
        self._validate_payload(payload)
        creation_payload = self._generate_creation_payload(payload)
        account = self.factory.create(creation_payload)
        return self._insert_account(account)

    def _validate_payload(self, payload: dict):
        errors = self.validator.validate_creation_payload(payload)
        if errors:
            raise AppDataValidationException(messages=errors)

    def _generate_creation_payload(self, payload: dict) -> dict:
        return {
            'username': payload['username'],
            'email': payload['email'],
            'hash_password': self.encryptor.encrypt_password(payload['password']),
            'email_confirmed': False
        }

    def _insert_account(self, account: Account) -> int:
        try:
            account_id = self.repository.insert(account)
        except EntityAlreadyExistsException:
            raise AppDataDuplicationException(messages='Account already exists')
        except PersitenceException:
            raise AppUnexpectedFailureException()
        else:
            return account_id
