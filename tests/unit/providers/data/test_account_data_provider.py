from unittest import mock
from unittest.mock import patch

import pytest
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from application.core.entity.account import Account
from application.core.exception.dashboardplus_exception import EntityAlreadyExistsException, PersitenceException
from application.providers.data import DatabaseAccessLayer
from application.providers.data.account_database_data_provider import AccountDatabaseDataProvider
from tests.base_tests import UnitTest


class TestAccountDatabaseProvider(UnitTest):
    def setup_method(self):
        self.mock_db = mock.create_autospec(DatabaseAccessLayer)
        self.provider = AccountDatabaseDataProvider(self.mock_db)
        self.account = Account(username='test', email='test', hash_password='mysecret', email_confirmed=False)

    def test_insert_should_add_an_account_object_to_session(self):
        # When
        self.provider.insert(self.account)

        # Then
        mapper = self.mock_db.session.add.call_args[0][0]
        assert mapper.username == 'test'
        assert mapper.email == 'test'
        assert mapper.hash_password == 'mysecret'
        assert mapper.email_confirmed is False

    def test_insert_should_commit_change(self):
        # When
        self.provider.insert(self.account)

        # Then
        self.mock_db.session.commit.assert_called_with()

    @patch('application.providers.data.account_database_data_provider.AccountMapper')
    def test_insert_should_return_account_identifier(self, mock_mapper):
        # Given
        self.account.id = 1
        mock_mapper.return_value = self.account

        # When
        actual = self.provider.insert(self.account)

        # Then
        assert 1 == actual

    def test_insert_should_raise_when_duplicate_records_is_found(self):
        # Given
        self.mock_db.session.commit.side_effect = IntegrityError(None, None, None)

        # When
        with pytest.raises(EntityAlreadyExistsException) as error:
            self.provider.insert(self.account)

        # Then
        assert "An entity Account is already created with fields ('email',)" == error.value.messages

    def test_insert_should_raise_when_unexpected_error_occured(self):
        # Given
        sql_error = SQLAlchemyError('error')
        self.mock_db.session.commit.side_effect = sql_error

        # When
        with pytest.raises(PersitenceException) as error:
            self.provider.insert(self.account)

        # Then
        assert sql_error == error.value.origins

    def test_does_account_exist_should_fetch_account_with_the_given_email(self):
        # When
        self.provider.does_account_exist('email')

        # Then
        self.mock_db.session.query().filter_by.assert_called_with(email='email')

    def test_does_account_exist_should_return_true_when_account_exist(self):
        # Given
        self.mock_db.session.query().filter_by().one_or_none.return_value = 'account'

        # When
        result = self.provider.does_account_exist('email')

        # Then
        assert result is True

    def test_does_account_exist_should_return_false_when_account_do_not_exist(self):
        # Given
        self.mock_db.session.query().filter_by().one_or_none.return_value = None

        # When
        result = self.provider.does_account_exist('email')

        # Then
        assert result is False

    def test_update_email_confirmed_should_update_account_with_the_given_email(self):
        # When
        self.provider.update_email_confirmed('email', True)

        # Then
        self.mock_db.session.query().filter_by.assert_called_with(email='email')
        self.mock_db.session.query().filter_by().update.assert_called_with({'email_confirmed': True})
