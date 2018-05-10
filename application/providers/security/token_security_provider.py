from itsdangerous import URLSafeTimedSerializer, BadData

from application.core.exception.dashboardplus_exception import UnexpectedFailureException
from application.core.port.create_safe_timed_token_port import CreateSafeTimedTokenPort


class TokenSecurityProvider(CreateSafeTimedTokenPort):
    def __init__(self, crypto: URLSafeTimedSerializer, config: dict):
        self.config = config
        self.crypto = crypto

    def create_safe_time_token(self, payload):
        try:
            return self.crypto.dumps(payload, salt=self.config['SECRET_KEY'])
        except BadData:
            raise UnexpectedFailureException()
