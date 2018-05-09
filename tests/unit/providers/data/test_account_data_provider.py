from unittest import mock
from unittest.mock import patch

import pytest
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from application.core.entity.account import Account
from application.core.exception.dashboardplus_exception import EntityAlreadyExistsException, PersitenceException
from application.providers.data import DatabaseAccessLayer
from application.providers.data.account_data_provider import AccountDataProvider
from tests.base_tests import UnitTest


class TestAccountDatabaseProvider(UnitTest):
    def setup_method(self):
        self.mock_db = mock.create_autospec(DatabaseAccessLayer)
        self.provider = AccountDataProvider(self.mock_db)
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

    @patch('application.providers.data.account_data_provider.AccountMapper')
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
