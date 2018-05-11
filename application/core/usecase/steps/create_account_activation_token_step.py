from application.core.port.create_account_activation_token_port import CreateAccountActivationTokenPort
from application.core.usecase.steps.base_step import BaseStep


class CreateAccountActivationTokenStep(BaseStep):
    def __init__(self, token_provider: CreateAccountActivationTokenPort):
        self.token_provider = token_provider

    def execute(self, payload):
        return self.token_provider.create_account_activation_token(payload)
