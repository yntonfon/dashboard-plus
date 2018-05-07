from marshmallow import Schema, fields, validate

from application.core.usecase.validate_new_account_payload_port import ValidateAccountCreationtPayloadPort


class AccountCreatingValidator(Schema):
    username = fields.String(
        required=True,
        allow_none=False,
        validate=validate.Length(min=1))
    email = fields.Email(
        required=True,
        allow_none=False)
    password = fields.String(
        required=True,
        allow_none=False,
        validate=validate.Length(min=1))


class AccountDataValidator(ValidateAccountCreationtPayloadPort):

    def validate_creation_payload(self, payload: dict) -> dict:
        validator = AccountCreatingValidator()
        return validator.validate(payload)
