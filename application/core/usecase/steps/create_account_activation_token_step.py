from application.core.port.create_safe_timed_token_port import CreateSafeTimedTokenPort
from application.core.usecase.steps.base_step import BaseStep


class CreateAccountActivationTokenStep(BaseStep):
    def __init__(self, token_provider: CreateSafeTimedTokenPort):
        self.token_provider = token_provider

    def execute(self, payload):
        return self.token_provider.create_safe_time_token(payload)
