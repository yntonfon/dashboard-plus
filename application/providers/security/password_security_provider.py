from application.core.port.encrypt_password_port import EncryptPasswordPort


class PasswordSecurityProvider(EncryptPasswordPort):
    def __init__(self, crypto, config):
        self.config = config
        self.crypto = crypto

    def encrypt_password(self, password: str) -> bytes:
        salt = self.config['SECRET_KEY'].encode()
        key_bytes = self.config['BCRYPT_DESIRED_KEY_BYTES']
        rounds = self.config['BCRYPT_ROUNDS']

        return self.crypto.kdf(password=password.encode(), salt=salt, desired_key_bytes=key_bytes, rounds=rounds)
