from unittest.mock import Mock

from application.providers.security.password_security_provider import PasswordSecurityProvider
from tests.base_tests import UnitTest


class TestPasswordSecurityProvider(UnitTest):
    def test_encrypt_password_should_call_kdf(self):
        # Given
        mock_bcrypt = Mock()
        mock_bcrypt.gensalt.return_value = 'salt'
        config = {
            'SECRET_KEY': 'mysecret',
            'BCRYPT_DESIRED_KEY_BYTES': 32,
            'BCRYPT_ROUNDS': 12
        }

        provider = PasswordSecurityProvider(mock_bcrypt, config)

        # When
        provider.encrypt_password('password')

        # Then
        mock_bcrypt.kdf.assert_called_with(password=b'password', salt=b'mysecret', desired_key_bytes=32, rounds=12)
