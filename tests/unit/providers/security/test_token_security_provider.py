from unittest import mock

import pytest
from itsdangerous import BadData, URLSafeTimedSerializer

from application.core.exception.dashboardplus_exception import UnexpectedFailureException
from application.providers.security.token_security_provider import TokenSecurityProvider


class TestTokenSecurityProvider:
    def setup_method(self):
        config = {'SECRET_KEY': 'mysecret', 'ACTIVATION_ACCOUNT_TOKEN_MAX_AGE': 10}
        self.mock_crypto = mock.create_autospec(URLSafeTimedSerializer)
        self.provider = TokenSecurityProvider(self.mock_crypto, config)

    def test_create_safe_time_token_should_call_dumps_on_crypto(self):
        # When
        self.provider.create_safe_time_token('payload')

        # Then
        self.mock_crypto.dumps.assert_called_with('payload', salt='mysecret')

    def test_create_safe_time_token_should_raise_when_error_occured(self):
        # Given
        self.mock_crypto.dumps.side_effect = BadData(message='error')

        # When
        with pytest.raises(UnexpectedFailureException):
            self.provider.create_safe_time_token('payload')

    def test_decode_activation_account_token_should_call_loads(self):
        # When
        self.provider.decode_activation_account_token('token')

        # Then
        self.mock_crypto.loads.assert_called_with('token', salt='mysecret', max_age=10)
