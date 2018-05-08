from application.core.entity.account import Account
from application.core.exception.dashboardplus_exception import (
    AppDataValidationException,
    EntityAlreadyExistsException,
    AppDataDuplicationException, PersitenceException,
    AppUnexpectedFailureException
)
from application.core.port.create_account_port import CreateAccountPort
from application.core.port.encrypt_password_port import EncryptPasswordPort
from application.core.port.insert_account_port import InsertAccountPort
from application.core.port.validate_account_payload_port import ValidateAccountPayloadPort


class CreateNewAccountUseCase:
    def __init__(self,
                 validator: ValidateAccountPayloadPort,
                 encryptor: EncryptPasswordPort,
                 factory: CreateAccountPort,
                 repository: InsertAccountPort):
        self.repository = repository
        self.factory = factory
        self.encryptor = encryptor
        self.validator = validator

    def execute(self, payload):
        self._validate_payload(payload)
        creation_payload = self._generate_creation_payload(payload)
        account = self.factory.create_account(creation_payload)
        return self._insert_account(account)

    def _validate_payload(self, payload: dict):
        errors = self.validator.validate_payload(payload)
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
