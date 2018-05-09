import pytest

from application.core.entity.account import Account
from application.core.exception.dashboardplus_exception import EntityAlreadyExistsException
from application.providers.data.account_data_mapper import AccountMapper
from application.providers.data.account_database_data_provider import AccountDatabaseDataProvider
from tests.base_tests import IntegrationTest


class TestAccountDatabaseProvider(IntegrationTest):
    def setup_method(self):
        super().setup_method()
        self.provider = AccountDatabaseDataProvider(self.db)

    def test_insert_should_create_a_new_records(self):
        # Given
        account = Account(username='test', email='test', hash_password='mysecret', email_confirmed=False)

        # When
        self.provider.insert(account)

        # Then
        saved_account = self.db.session.query(AccountMapper).first()
        assert account.username == saved_account.username

    def test_insert_should_raise_when_records_already_exist(self):
        # Given
        account = Account(username='test', email='test', hash_password='mysecret', email_confirmed=False)

        # When
        with pytest.raises(EntityAlreadyExistsException):
            self.provider.insert(account)
            self.provider.insert(account)
