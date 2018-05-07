import bcrypt

from application.core.usecase.encrypt_password_port import EncryptPasswordPort

ENCRYPTION_LOG_ROUNDS = 12


class PasswordSecurityProvider(EncryptPasswordPort):

    def encrypt_password(self, password: str):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt(ENCRYPTION_LOG_ROUNDS))
