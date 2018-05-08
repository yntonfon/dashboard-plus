from application.providers.validator.account_schema import AccountSchema
from tests.base_tests import UnitTest


class TestAccountSchema(UnitTest):
    def setup_method(self):
        self.schema = AccountSchema()
        self.payload = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }

    def test_validate_returns_error_when_username_are_missing(self):
        # Given
        self.payload.pop('username')

        # When
        errors = self.schema.validate(self.payload)

        # Then
        assert 'username' in errors

    def test_validate_returns_error_when_username_is_none(self):
        # Given
        self.payload.update(**{'username': None})

        # When
        errors = self.schema.validate(self.payload)

        # Then
        assert 'username' in errors

    def test_validate_returns_error_when_username_is_empty(self):
        # Given
        self.payload.update(**{'username': ''})

        # When
        errors = self.schema.validate(self.payload)

        # Then
        assert 'username' in errors

    def test_validate_returns_error_when_email_are_missing(self):
        # Given
        self.payload.pop('email')

        # When
        errors = self.schema.validate(self.payload)

        # Then
        assert 'email' in errors

    def test_validate_returns_error_when_email_is_none(self):
        # Given
        self.payload.update(**{'email': None})

        # When
        errors = self.schema.validate(self.payload)

        # Then
        assert 'email' in errors

    def test_validate_returns_error_when_email_is_not_valid(self):
        # Given
        self.payload.update(**{'email': 'not_valid'})

        # When
        errors = self.schema.validate(self.payload)

        # Then
        assert 'email' in errors

    def test_validate_returns_error_when_password_are_missing(self):
        # Given
        self.payload.pop('password')

        # When
        errors = self.schema.validate(self.payload)

        # Then
        assert 'password' in errors

    def test_validate_returns_error_when_password_is_none(self):
        # Given
        self.payload.update(**{'password': None})

        # When
        errors = self.schema.validate(self.payload)

        # Then
        assert 'password' in errors

    def test_validate_returns_error_when_password_is_empty(self):
        # Given
        self.payload.update(**{'password': ''})

        # When
        errors = self.schema.validate(self.payload)

        # Then
        assert 'password' in errors
