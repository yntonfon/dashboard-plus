from unittest import mock

from application.core.port.create_account_activation_token_port import CreateAccountActivationTokenPort
from application.core.usecase.steps.create_account_activation_token_step import (
    CreateAccountActivationTokenStep
)


class TestCreateAccountActivationTokenStep:
    def test_should_call_create_safe_time_token_on_the_provider(self):
        # Given
        mock_token_provider = mock.create_autospec(CreateAccountActivationTokenPort)
        step = CreateAccountActivationTokenStep(mock_token_provider)

        # When
        step.execute('data')

        # Then
        mock_token_provider.create_account_activation_token.assert_called_with('data')
