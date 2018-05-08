from marshmallow import Schema, fields, validate


class AccountSchema(Schema):
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
