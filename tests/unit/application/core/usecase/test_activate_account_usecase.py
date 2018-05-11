from unittest import mock

from application.core.exception.dashboardplus_exception import PersitenceException
from application.core.port.decode_safe_time_token_port import DecodeActivationAccountTokenPort
from application.core.port.does_account_exist_port import DoesAccountExistPort
from application.core.port.update_email_confirmed_port import UpdateEmailConfirmedPort
from application.core.usecase import ActivateAccountUseCase
from application.core.usecase.usecase_input import UseCaseInput
from application.core.usecase.usecase_output import (
    UseCaseStatusEnum, UseCaseMessageEnum,
    UseCaseDescriptionEnum
)
from tests.base_tests import UnitTest


class TestActivateAccountUseCase(UnitTest):
    def setup_method(self):
        self.mock_decode_token_provider = mock.create_autospec(DecodeActivationAccountTokenPort)
        self.mock_does_account_exist_provider = mock.create_autospec(DoesAccountExistPort)
        self.mock_update_email_confirmed_provider = mock.create_autospec(UpdateEmailConfirmedPort)
        self.usecase = ActivateAccountUseCase(self.mock_decode_token_provider,
                                              self.mock_does_account_exist_provider,
                                              self.mock_update_email_confirmed_provider)
        self.usecase_input = UseCaseInput(payload='token')

    def test_should_call_decode_safe_timed_token(self):
        # When
        self.usecase.handle(self.usecase_input)

        # Then
        self.mock_decode_token_provider.decode_activation_account_token.assert_called_with('token')

    def test_should_call_update_email_confirmed_if_an_account_exits_with_the_given_email(self):
        # Given
        self.mock_decode_token_provider.decode_activation_account_token.return_value = 'email'
        self.mock_does_account_exist_provider.does_account_exist.return_value = True

        # When
        self.usecase.handle(self.usecase_input)

        # Then
        self.mock_update_email_confirmed_provider.update_email_confirmed.assert_called_with('email', True)

    def test_should_return_success_output_when_account_is_activated(self):
        # Given
        self.mock_does_account_exist_provider.does_account_exist.return_value = True

        # When
        usecase_output = self.usecase.handle(self.usecase_input)

        # Then
        assert UseCaseStatusEnum.success == usecase_output.status
        assert UseCaseMessageEnum.account_activated == usecase_output.message

    def test_should_return_failure_output_when_decoding_token_failed(self):
        # Given
        self.mock_decode_token_provider.decode_activation_account_token.return_value = None

        # When
        usecase_output = self.usecase.handle(self.usecase_input)

        # Then
        assert UseCaseStatusEnum.failure == usecase_output.status
        assert UseCaseMessageEnum.account_not_activated == usecase_output.message
        assert UseCaseDescriptionEnum.invalid_token == usecase_output.description

    def test_should_return_failure_output_when_account_do_not_exist(self):
        # Given
        self.mock_does_account_exist_provider.does_account_exist.return_value = False

        # When
        usecase_output = self.usecase.handle(self.usecase_input)

        # Then
        assert UseCaseStatusEnum.failure == usecase_output.status
        assert UseCaseMessageEnum.account_not_activated == usecase_output.message
        assert UseCaseDescriptionEnum.account_does_not_exist == usecase_output.description

    def test_should_return_failure_output_when_does_account_exist_provider_throw_error(self):
        # Given
        self.mock_does_account_exist_provider.does_account_exist.side_effect = PersitenceException()

        # When
        usecase_output = self.usecase.handle(self.usecase_input)

        # Then
        assert UseCaseStatusEnum.failure == usecase_output.status
        assert UseCaseMessageEnum.account_not_activated == usecase_output.message
        assert UseCaseDescriptionEnum.unexpected_error == usecase_output.description

    def test_should_return_failure_output_when_update_email_confirmed_provider_throw_error(self):
        # Given
        self.mock_update_email_confirmed_provider.update_email_confirmed.side_effect = PersitenceException()

        # When
        usecase_output = self.usecase.handle(self.usecase_input)

        # Then
        assert UseCaseStatusEnum.failure == usecase_output.status
        assert UseCaseMessageEnum.account_not_activated == usecase_output.message
        assert UseCaseDescriptionEnum.unexpected_error == usecase_output.description
