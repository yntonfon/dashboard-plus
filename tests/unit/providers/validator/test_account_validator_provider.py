from unittest import mock

from application.providers.validator.account_validator_provider import AccountValidatorProvider
from application.providers.validator.schema.account_schema import AccountSchema
from tests.base_tests import UnitTest


class TestAccountValidatorProvider(UnitTest):
    def test_validate_payload_should_call_validate(self):
        # Given
        mock_schema = mock.create_autospec(AccountSchema)
        validator = AccountValidatorProvider(mock_schema)

        # When
        validator.validate_payload({})

        # Then
        mock_schema.validate.assert_called_with({})
