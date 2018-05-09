from unittest.mock import Mock

from application.providers.security.password_security_provider import PasswordSecurityProvider
from tests.base_tests import UnitTest


class TestPasswordSecurityProvider(UnitTest):
    def test_encrypt_password_should_call_hashpw(self):
        # Given
        mock_bcrypt = Mock()
        mock_bcrypt.gensalt.return_value = 'salt'
        provider = PasswordSecurityProvider(mock_bcrypt)

        # When
        provider.encrypt_password('password')

        # Then
        mock_bcrypt.hashpw.assert_called_with(b'password', 'salt')
