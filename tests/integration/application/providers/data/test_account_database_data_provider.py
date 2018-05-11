import pytest

from application.core.entity.account import Account
from application.core.exception.dashboardplus_exception import EntityAlreadyExistsException
from application.providers.data.account_data_mapper import AccountMapper
from application.providers.data.account_database_data_provider import AccountDatabaseDataProvider
from tests.base_tests import IntegrationTest


class TestAccountDatabaseDataProvider(IntegrationTest):
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

    def test_does_account_exist_should_return_true_when_account_exist(self):
        # Given
        account = AccountMapper(email='test@test.com')
        self.db.session.add(account)
        self.db.session.commit()

        # When
        result = self.provider.does_account_exist('test@test.com')

        # Then
        assert result is True

    def test_does_account_exist_should_return_false_when_account_do_no_exist(self):
        # Given
        account = AccountMapper(email='test@test.com')
        self.db.session.add(account)
        self.db.session.commit()

        # When
        result = self.provider.does_account_exist('notfound@test.com')

        # Then
        assert result is False

    def test_update_email_confirmed(self):
        # Given
        account = AccountMapper(email='test@test.com', email_confirmed=False)
        self.db.session.add(account)
        self.db.session.commit()

        # When
        self.provider.update_email_confirmed('test@test.com', True)

        # Then
        assert account.email_confirmed is True
