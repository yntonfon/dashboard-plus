from application.configuration.ioc_providers import IOCProviders
from application.core.factory.account_factory import AccountFactory
from application.core.usecase.create_new_account_use_case import CreateNewAccountUseCase
from application.providers.data.account_data_mapper import AccountMapper
from application.providers.data.account_data_provider import AccountDataProvider
from tests.base_tests import E2ETest


class TestCreateAccountHappyPath(E2ETest):
    def test_succesfully_create_a_new_account(self):
        # Given
        input_payload = {
            'username': 'Bertrand',
            'email': 'bertrand@test.com',
            'password': 'Password01!'
        }
        account_validator_provider = IOCProviders.account_validator_provider()
        pwd_security_provider = IOCProviders.password_security_provider()
        factory = AccountFactory()
        repository = AccountDataProvider(self.db.session)
        use_case = CreateNewAccountUseCase(account_validator_provider, pwd_security_provider, factory, repository)

        # When
        use_case.execute(input_payload)

        # Then
        account = self.db.session.query(AccountMapper).first()
        assert 1 == account.id
        assert 'Bertrand' == account.username
