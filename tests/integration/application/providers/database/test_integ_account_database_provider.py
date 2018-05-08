import pytest

from application.core.entity.account import Account
from application.core.exception.dashboardplus_exception import EntityAlreadyExistsException
from application.providers.database import DatabaseAccessLayer
from application.providers.database.account_database_provider import AccountDatabaseProvider
from application.providers.database.mapper.account_mapper import AccountMapper


class TestIntegAccountDatabaseProvider:
    def setup_class(cls):
        cls.db = DatabaseAccessLayer()
        cls.db.db_init('sqlite:////tmp/:test-dashboard-plus:')

    def teardown_class(cls):
        cls.db.db_drop()

    def setup_method(self):
        self.provider = AccountDatabaseProvider(self.db)

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
