from application.core.usecase.encrypt_password_port import EncryptPasswordPort

ENCRYPTION_LOG_ROUNDS = 12


class PasswordSecurityProvider(EncryptPasswordPort):
    def __init__(self, crypto):
        self.crypto = crypto

    def encrypt_password(self, password: str):
        return self.crypto.hashpw(password.encode(), self.crypto.gensalt(ENCRYPTION_LOG_ROUNDS))
