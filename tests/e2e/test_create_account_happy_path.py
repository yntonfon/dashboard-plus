import bcrypt

from application.core.factory.account_factory import AccountFactory
from application.core.usecase.create_new_account_use_case import CreateNewAccountUseCase
from application.providers.data.account_data_mapper import AccountMapper
from application.providers.data.account_data_provider import AccountDatabaseProvider
from application.providers.security.password_security_provider import PasswordSecurityProvider
from application.providers.validator.account_schema import AccountSchema
from application.providers.validator.account_validator_provider import AccountValidatorProvider
from tests.base_tests import E2ETest


class TestCreateAccountHappyPath(E2ETest):
    def test_succesfully_create_a_new_account(self):
        # Given
        input_payload = {
            'username': 'Bertrand',
            'email': 'bertrand@test.com',
            'password': 'Password01!'
        }
        schema = AccountSchema()
        validator = AccountValidatorProvider(schema)
        encryptor = PasswordSecurityProvider(bcrypt)
        factory = AccountFactory()
        repository = AccountDatabaseProvider(self.db)
        use_case = CreateNewAccountUseCase(validator, encryptor, factory, repository)

        # When
        use_case.execute(input_payload)

        # Then
        account = self.db.session.query(AccountMapper).first()
        assert 1 == account.id
        assert 'Bertrand' == account.username