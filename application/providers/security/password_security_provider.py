from application.core.port.encrypt_password_port import EncryptPasswordPort


class PasswordSecurityProvider(EncryptPasswordPort):
    def __init__(self, crypto):
        self.crypto = crypto

    def encrypt_password(self, password: str):
        return self.crypto.hashpw(password.encode(), self.crypto.gensalt())
