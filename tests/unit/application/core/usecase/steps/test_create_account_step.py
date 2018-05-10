from unittest import mock
from unittest.mock import Mock

import pytest

from application.core.exception.dashboardplus_exception import (
    InputValidationException, EntityAlreadyExistsException,
    AccountAlreadyExistsException, PersitenceException, AppUnexpectedFailureException
)
from application.core.factory.account_factory import AccountFactory
from application.core.port.encrypt_password_port import EncryptPasswordPort
from application.core.port.insert_account_port import InsertAccountPort
from application.core.port.validate_account_payload_port import ValidateAccountPayloadPort
from application.core.usecase.steps.create_account_step import CreateAccountStep


class TestCreateNewAccountUseCase:
    def setup_method(self):
        self.validator = mock.create_autospec(ValidateAccountPayloadPort)
        self.encryptor = mock.create_autospec(EncryptPasswordPort)
        self.factory = mock.create_autospec(AccountFactory)
        self.repository = mock.create_autospec(InsertAccountPort)
        self.use_case = CreateAccountStep(self.validator, self.encryptor, self.factory, self.repository)
        self.payload = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'mysecret'
        }

        # Configure mock
        self.validator.validate_payload.return_value = {}

    def test_returns_the_identifier_of_the_new_account(self):
        # Given
        account_id = 1
        self.repository.insert.return_value = account_id

        # When
        actual = self.use_case.execute(self.payload)

        # Then
        assert account_id == actual

    def test_validates_constraint_on_the_given_payload(self):
        # When
        self.use_case.execute(self.payload)

        # Then
        self.validator.validate_payload.assert_called_with(self.payload)

    def test_encrypts_password(self):
        # When
        self.use_case.execute(self.payload)

        # Then
        self.encryptor.encrypt_password.assert_called_with('mysecret')

    def test_creates_new_account(self):
        # Given
        self.encryptor.encrypt_password.return_value = 'myhashsecret'
        expected = {
            'username': 'test',
            'email': 'test@test.com',
            'hash_password': 'myhashsecret',
            'email_confirmed': False
        }

        # When
        self.use_case.execute(self.payload)

        # Then
        self.factory.create_account.assert_called_with(expected)

    def test_saves_the_new_account(self):
        # Given
        account = Mock()
        self.factory.create_account.return_value = account

        # When
        self.use_case.execute(self.payload)

        # Then
        self.repository.insert.assert_called_with(account)

    def test_raises_error_when_payload_is_invalid(self):
        # Given
        self.validator.validate_payload.return_value = {'errors occured'}

        # When
        with pytest.raises(InputValidationException) as error:
            self.use_case.execute(self.payload)

        # Then
        assert {'errors occured'} == error.value.messages

    def test_raises_error_when_account_already_exists(self):
        # Given
        self.repository.insert.side_effect = EntityAlreadyExistsException('', ())

        # When
        with pytest.raises(AccountAlreadyExistsException) as error:
            self.use_case.execute(self.payload)

        # Then
        assert "Account already exists" == error.value.messages

    def test_raises_error_when_account_insertion_failed(self):
        # Given
        self.repository.insert.side_effect = PersitenceException()

        # When
        with pytest.raises(AppUnexpectedFailureException):
            self.use_case.execute(self.payload)
