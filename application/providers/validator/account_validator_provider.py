from application.core.port.validate_account_payload_port import ValidateAccountPayloadPort


class AccountValidatorProvider(ValidateAccountPayloadPort):
    def __init__(self, schema):
        self.schema = schema

    def validate_payload(self, payload):
        return self.schema.validate(payload)
