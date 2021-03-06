import abc


class EncryptPasswordPort(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def encrypt_password(self, password: str) -> bytes:
        raise NotImplementedError('users must define encrypt_password to use this base class')
