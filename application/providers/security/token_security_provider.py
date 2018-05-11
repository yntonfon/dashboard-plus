from itsdangerous import URLSafeTimedSerializer, BadData

from application.core.exception.dashboardplus_exception import UnexpectedFailureException
from application.core.port.create_safe_timed_token_port import CreateSafeTimedTokenPort
from application.core.port.decode_safe_time_token_port import DecodeActivationAccountTokenPort


class TokenSecurityProvider(CreateSafeTimedTokenPort, DecodeActivationAccountTokenPort):
    def __init__(self, crypto: URLSafeTimedSerializer, config: dict):
        self.config = config
        self.crypto = crypto

    def create_safe_time_token(self, payload):
        try:
            return self.crypto.dumps(payload, salt=self.config['SECRET_KEY'])
        except BadData:
            raise UnexpectedFailureException()

    def decode_activation_account_token(self, token: str) -> object:
        return self.crypto.loads(token,
                                 salt=self.config['SECRET_KEY'],
                                 max_age=self.config['ACTIVATION_ACCOUNT_TOKEN_MAX_AGE'])
