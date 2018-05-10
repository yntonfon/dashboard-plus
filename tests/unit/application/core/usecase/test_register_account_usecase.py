from unittest import mock

from application.core.exception.dashboardplus_exception import (
    InputValidationException, UnexpectedFailureException,
    AccountAlreadyExistsException
)
from application.core.usecase import RegisterAccountUseCase
from application.core.usecase.steps import CreateAccountStep
from application.core.usecase.usecase_input import UsecaseInput
from application.core.usecase.usecase_output import UsecaseStatusEnum, UsecaseMessageEnum
from tests.base_tests import UnitTest


class TestRegisterAccountUsecase(UnitTest):
    def setup_method(self):
        self.mock_create_account_step = mock.create_autospec(CreateAccountStep)
        self.usecase = RegisterAccountUseCase(self.mock_create_account_step)
        self.usecase_input = UsecaseInput(payload='a payload')

    def test_should_execute_creation_account_step(self):
        # When
        self.usecase.handle(self.usecase_input)

        # Then
        self.mock_create_account_step.execute.assert_called_with('a payload')

    def test_returns_output_error_when_a_validation_error_is_thrown(self):
        # Given
        self.mock_create_account_step.execute.side_effect = InputValidationException(messages='help')

        # Then
        usecase_output = self.usecase.handle(self.usecase_input)

        #
        assert UsecaseStatusEnum.failure == usecase_output.status
        assert UsecaseMessageEnum.invalid_input_data == usecase_output.message
        assert 'help' == usecase_output.description

    def test_returns_output_error_when_an_account_already_exists_exception_is_thrown(self):
        # Given
        self.mock_create_account_step.execute.side_effect = AccountAlreadyExistsException()

        # Then
        usecase_output = self.usecase.handle(self.usecase_input)

        #
        assert UsecaseStatusEnum.failure == usecase_output.status
        assert UsecaseMessageEnum.account_already_exists == usecase_output.message

    def test_returns_output_error_when_an_unexpected_error_is_thrown(self):
        # Given
        self.mock_create_account_step.execute.side_effect = UnexpectedFailureException()

        # Then
        usecase_output = self.usecase.handle(self.usecase_input)

        #
        assert UsecaseStatusEnum.failure == usecase_output.status
        assert UsecaseMessageEnum.unexpected_error == usecase_output.message
